from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


class DynamicLabelsApp(App):
    """Main app to dynamically create labels."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Li", "Zheng", "Yuan"]

    def build(self):
        """Build the Kivy GUI."""
        self.root = Builder.load_file("dynamic_labels.kv")

        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)

        return self.root

DynamicLabelsApp().run()