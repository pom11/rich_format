import types
from rich.text import Text, Span
from rich.style import Style
from string import Formatter
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    NamedTuple,
    Optional,
    Tuple,
    Union,
)

def _format(self, *args, **kwargs) -> "Text":
    """Return a new Text instance with formatted specified value(s) and insert them inside the string's placeholder"""

    def get_newtext_w_style_from_index(
        string: str, index: int, texts_list: List[Text]
    ) -> "Text":
        text = texts_list[index]
        return Text(
            string,
            style=text.style,
            justify=text.justify,
            overflow=text.overflow,
            no_wrap=text.no_wrap,
            end=text.end,
            tab_size=text.tab_size,
            spans=text.spans,
        )

    copy = self.copy()
    # get fields to substitute
    initial_parsing = [fields for fields in Formatter().parse(self.plain)]
    # if there is nothing to substitute return copy
    if len(initial_parsing) == 1 and initial_parsing[0][1] == None:
        return copy
    # this will be returned as a final result
    formatted = Text()
    # how much of the initial length was parsed
    parsed_len = 0
    # arg as strings even for Text params
    _args = [text.plain if type(text) == Text else text for text in list(args)]
    # kwargs as strings even for Text params
    _kwargs = {
        key: text.plain if type(text) == Text else text
        for key, text in kwargs.items()
    }
    # substitute only if there are args or kwargs
    if len(args) != 0 or len(_kwargs) != 0:
        # get {0} number type placeholders
        field_numbers = [
            "{"
            + field_name
            + f'{":"+format_spec if format_spec not in [None,""] else ""}'
            + f'{"!"+conversion if conversion not in [None,""] else ""}'
            + "}"
            for literal_text, field_name, format_spec, conversion in initial_parsing
            if field_name and field_name.isdigit()
        ]
        # get {} brackets type placeholders
        field_brackets = [
            "{"
            + field_name
            + f'{":"+format_spec if format_spec not in [None,""] else ""}'
            + f'{"!"+conversion if conversion not in [None,""] else ""}'
            + "}"
            for literal_text, field_name, format_spec, conversion in initial_parsing
            if field_name != None and not field_name.isdigit() and field_name == ""
        ]
        # raise standard type error, {0} and {} can't coexist
        if len(field_numbers) != 0 and len(field_brackets) != 0:
            raise TypeError(
                "Cannot switch from manual field specification to automatic field numbering"
            )
        # parse fields to substitute
        for literal_text, field_name, format_spec, conversion in initial_parsing:
            # partial Text of literal_text - get substring from parsed_len till end of literal_text
            split_at = parsed_len
            # as Formatter replaces double brackets with single brackets we need to add "count" to split_at
            split_at += formatted.divide([parsed_len])[0].plain.count("{")
            split_at += formatted.divide([parsed_len])[0].plain.count("}")
            formatted_partially = copy.divide([split_at])[1].divide(
                [len(literal_text)]
            )[0]
            # if there is something to substitute
            if field_name != None:
                format_spec = "" if format_spec in [None, ""] else f":{format_spec}"
                conversion = "" if conversion in [None, ""] else f"!{conversion}"
                # field to substitute
                to_replace = "{" + field_name + format_spec + conversion + "}"
                # result after substitution
                new_string = to_replace.format(*tuple(_args), **_kwargs)
                # get Spans for replaced string
                start_index = self.plain.index(to_replace, parsed_len)
                end_index = start_index + len(to_replace)
                spans = [
                    Span(start=0, end=len(new_string), style=span.style)
                    for span in self._spans
                    if start_index <= span.start <= end_index
                    or start_index <= span.end <= end_index
                ]
                # init new text with style
                new_text = Text(
                    new_string,
                    style=self.style,
                    justify=self.justify,
                    overflow=self.overflow,
                    no_wrap=self.no_wrap,
                    end=self.end,
                    tab_size=self.tab_size,
                    spans=spans,
                )
                # check either kwargs or args is used
                # if in kwargs
                if field_name in kwargs.keys():
                    # check if param is Text
                    if type(kwargs[field_name]) == Text:
                        # replace new_text with provided Text
                        new_text = get_newtext_w_style_from_index(
                            new_string,
                            list(kwargs.keys()).index(field_name),
                            list(kwargs.values()),
                        )
                # if in args
                else:
                    # if is {0} placeholder
                    if str(field_name).isdigit():
                        # check if param is Text
                        if type(list(args)[int(field_name)]) == Text:
                            # replace new_text with provided Text
                            new_text = get_newtext_w_style_from_index(
                                new_string, int(field_name), list(args)
                            )
                    # if is {} placeholder
                    else:
                        # check if param is Text
                        if type(list(args)[0]) == Text:
                            # replace new_text with provided Text
                            new_text = get_newtext_w_style_from_index(
                                new_string, 0, list(args)
                            )
                        _args.pop(0)
                        args = tuple(list(args)[1:])
                # add replaced value to formatted_partially
                formatted_partially.append_text(new_text)
                # keep track how much of plain we parsed
                parsed_len += len(to_replace)
            # add to end result
            formatted.append_text(formatted_partially)
            # keep track how much of plain we parsed
            parsed_len += len(literal_text)
    if formatted != Text():
        return formatted
    return copy

Text.format = _format
