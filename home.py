from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, OptionList

from article_screen import ArticleScreen


class HomeScreen(Screen[None]):

    CSS_PATH = ['home_layout.tcss', 'article_layout.tcss']

    def compose(self) -> ComposeResult:
        yield Header()
        yield OptionList(*['1', '2'], id='sidebar-feeds', classes='sidebar-expanded')
        yield OptionList(*[], id='sidebar-articles', classes='sidebar-collapsed')
        yield ArticleScreen("Hello")
        yield Footer()
