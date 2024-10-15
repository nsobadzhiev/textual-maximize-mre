from textual.app import App

from home import HomeScreen


class MRE(App[None]):

    async def on_mount(self) -> None:
        await self.push_screen(HomeScreen())


def run_app():
    app = MRE()
    app.run()


if __name__ == '__main__':
    run_app()
