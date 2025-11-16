from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


class DynamicLabelsApp(App):
    """Main app to dynamically create labels."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Li", "Zheng", "Yuan"]



DynamicLabelsApp().run()