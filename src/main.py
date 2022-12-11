from kivy.app import App
from datetime import datetime
from datetime import timedelta
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.metrics import dp
import kivy

#kivy.require('1.9.0')

from kivy.config import Config



Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '100')


class ClockApp(App):
    def build(self):
        self.icon = "clock.png"
        self.now = datetime.now()

        # Schedule the self.update_clock function to be called once a second
        Clock.schedule_interval(self.update_clock, 1)
        self.my_label = Label(color=(1, .5, 1, 1), text=self.now.strftime('%H:%M:%S'), font_name="..\\fonts\\Lcd.ttf",
                              font_size=dp(50))
        return self.my_label  # The label is the only widget in the interface

    def update_clock(self, *args):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.now = self.now + timedelta(seconds=1)
        self.my_label.text = self.now.strftime('%H:%M:%S')


ClockApp().run()
