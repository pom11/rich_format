def console_test():
	from rich.text import Text, Span
	from rich.style import Style
	from rich.console import Console
	import datetime
	c = Console()

	t = Text("Hello {name}",style="red on white")
	tt = t.format(name="pom11")
	c.print(t)
	c.print(tt)

	t = Text("Hello {{name}} {{test}} welcome",style="red on white")
	tt = t.format(name="pom11",test="test2")
	c.print(t)
	c.print(tt)

	t = Text.from_markup("Hello [b]{name}[/]")
	tt = t.format(name=Text.from_markup("[red]pom11[/]"))
	c.print(t)
	c.print(tt)

	t = Text.from_markup("Hello [b]{name:.8}[/] [yellow]{greeting}[/] how [blue]{verb}[/] are you?")
	tt = t.format(name="pom11"*5,greeting="welcome",verb=Text.from_markup('[black on green]busy[/]'))
	c.print(t)
	c.print(tt)

	t = Text.from_ansi("Hello \x1b[30;43;5m{name}\x1b[0m \x1b[30;45;22m{greeting}\x1b[0m")
	tt = t.format(name=Text.from_markup(f"[black on white]{'pom11'*2}[/][red on white]{'pom11'*3}[/]"),greeting='welcome')
	c.print(t)
	c.print(tt)

	t = Text("Hello {name} {greeting}  ",spans=[Span(0,15,"black on yellow"),Span(6,12,"black on magenta"),Span(15,16,"black on red")])
	tt = t.format(name="pom11"*5,greeting='welcome')
	c.print(t)
	c.print(tt)

	t = Text.from_markup("Hello [b]{}[/] [red]{}[/]")
	tt = t.format("pom11",Text.from_markup("[black on cyan]welcome[/]"))
	c.print(t)
	c.print(tt)

	t = Text.from_markup("Hello [b]{:2}[/] [red]{:3}[/] how are you?")
	tt = t.format("pom11","welcome")
	c.print(t)
	c.print(tt)

	t = Text.from_markup("Hello [b]{0}[/] [red]{1}[/]")
	tt = t.format("pom11","welcome")
	c.print(t)
	c.print(tt)

	t = Text.from_markup("Hello [b]{1}[/] [red]{0}[/]")
	tt = t.format("pom11","welcome")
	c.print(t)
	c.print(tt)

	t = Text.from_markup("Hello [b]{}[/] [red]{}[/]")
	tt = t.format("pom11","welcome")
	c.print(t)
	c.print(tt)

	t = Text.from_markup("Hello [b]{:^10.2f}[/] [red]{}[/]")
	tt = t.format(420.420,"welcome")
	c.print(t)
	c.print(tt)

	t = Text.from_markup("Hello [underline black on white]{0:0.0f}[/] [red]{1}[/]")
	tt = t.format(420.420,"welcome")
	c.print(t)
	c.print(tt)

	t = Text.from_markup("Hello [b]{0:.2%}[/] [red]{1:.0%}[/]")
	tt = t.format(0.5,0.5)
	c.print(t)
	c.print(tt)

	t = Text.from_markup("Hello [b]{0:d}[/] [b]{0:x}[/] [b]{0:o}[/] [b]{0:b}[/]")
	tt = t.format(42)
	c.print(t)
	c.print(tt)

	t = Text.from_markup("Hello [b]{}[/] [red]{0}[/]")
	c.print(t)
	tt = t.format("pom11","welcome")
	c.print(tt)