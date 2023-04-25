# rich_format
[![PyPI](https://img.shields.io/pypi/v/rich_format.svg)](https://pypi.org/project/rich_format/) [![PyPI](https://img.shields.io/pypi/pyversions/rich_format.svg)](https://img.shields.io/pypi/pyversions/rich_format.svg)

`rich_format` replicates python string formatting for rich `Text` instances adding the possibility to substitute also with `Text`.

```python
>>> from rich.console import Console
>>> from rich.text import Text
>>> import rich_format
>>> console = Console()
>>> text = Text("Hello {name}",style="red on white")
>>> formatted_text = t.format(name=Text("pom11"))
>>> console.print(text)
Hello {name}
>>> console.print(formatted_text)
Hello pom11
```
See more examples running `rich_format.test`  or inspect [this](https://github.com/pom11/rich_format/blob/main/rich_format/test.py).


## Usage
First you need to import `Text` from rich so that `rich_format` works.
```python
from rich.text import Text
import rich_format
```

### Textual
You can use `rich_format` in `textual` to format easier `reactive` in custom widgets

`rich_format.demo`

```python
from textual.reactive import reactive
from textual.app import App, ComposeResult
from textual.widgets import Footer
from textual.widgets import Static
from rich.text import Text
import rich_format
import random

city = [
    Text.from_markup("from [blue on red]London[/]"),
    Text.from_markup("from [magenta on blue]New York[/]"),
    Text.from_markup("from [green]Bucharest[/]"),
    Text.from_markup("from [red on white]Tokyo[/]")
]

class CustomHeader(Static):
    banner : Text = reactive(Text(""))
    world : str = reactive("")

    def __init__(self, template: str) -> None:
        self.template = template
        super().__init__()

    def watch_banner(self, banner: Text) -> None:
        self.update(banner)

    def watch_world(self, world: str) -> None:
        self.banner = Text(self.template).format(world=world)

class DemoApp(App):

    BINDINGS = [
    ("q","quit","Quit"),
    ("h", "toggle_header", "Random header")
    ]

    def compose(self) -> ComposeResult:
        yield CustomHeader(template="Hello {world}")
        yield Footer()

    def action_toggle_header(self) -> None:
        widget = self.query_one(CustomHeader)
        widget.world = random.choice(city)


if __name__ == "__main__":
    app = DemoApp()
    app.run()
```

## Installation
### Stable release - pypi
To install `rich_format` run this command in your terminal
```bash
pip install rich_format
```
### From sources
The sources for rich_format can be downloaded from [Github](https://github.com/pom11/rich_format)
* clone the public repository
```bash
git clone https://github.com/pom11/rich_format
```
* install from source
```bash
python setup.py install
```

