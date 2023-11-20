from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class SimpleApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Hello, World!', font_size=30)
        layout.add_widget(label)
        return layout

if __name__ == '__main__':
    SimpleApp().run()
