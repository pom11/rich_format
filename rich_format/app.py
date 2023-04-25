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


def run():
	app = DemoApp()
	app.run()