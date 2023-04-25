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

