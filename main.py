from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import langdetect as detect
from deep_translator import GoogleTranslator
import pyttsx3
from langcodes import Language


class MainApp(App):

    def __init__(self, **kwargs):
        super(MainApp, self).__init__()
        self.i_lable = None
        self.button = None
        self.insert = None
        self.my_widget = None
        self.s_detect = None
        self.text_ = None
        self.s_text = None
        self.type_font = None
        self.font = ["Hindi,Gujrati\nGurumukhi,Tamil,Kannad\nMalyalam,\nodia,Telgu", "Japnees", "Latin, Greek\nArbik",
                     "Korian"]
        self.but2 = []

    def build(self):
        # drop_down = DropDown()
        # for i in range(len(self.font)):
        #     btton = Button(text=self.font[i],  size_hint=(None, None), pos=(350, 300),pos_hint={"center_x": 0, "center_y": 0.25},width=250)
        #     btton.bind(on_select = lambda btton: drop_down.select(btton.on_press))
        #     drop_down.add_widget(btton)
        main_button = Button(text='Select Font', size_hint=(0.27, 1))
        # for i in range(4):
        #     x = self.font_name(i)
        #     drop_down.bind(on_select=lambda instance, x: setattr(btton, "on_press", x))
        main_button.bind(on_release=self.selct_font)
        self.cols = 3
        self.icon = "icon.jpg"
        self.enter = Label(text='Enter your text here', width=10, font_size=30,
                           pos_hint={"center_x": 0.5, "center_y": 0.5})
        self.s_text = TextInput(font_name="Nirmala")
        self.main_layout = BoxLayout(orientation="vertical")
        self.main_layout.add_widget(main_button)
        self.main_layout.add_widget(self.enter)
        self.main_layout.add_widget(self.s_text)

        buttons = [
            ["Detect language", "Translate english to Hindi"],
            ["text to speech", "translate to english"],
        ]
        but = []
        for row in buttons:
            h_layout = BoxLayout()
            for lable in row:
                button = Button(
                    text=lable, font_size=30, background_color="red",
                    pos_hint={"center_x": 0.5, "center_y": 0.5}
                )
                but.append(button)
                h_layout.add_widget(button)
            self.main_layout.add_widget(h_layout)
        button1 = Button(
            text="clear", font_size=30, background_color="red",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        self.main_layout.add_widget(button1)
        button1.bind(on_press=self.clear)
        for i in range(len(but)):
            if (i == 0):
                but[i].bind(on_press=self.detectLanguage)
            if (i == 2):
                but[i].bind(on_press=self.text_to_speech)
            if (i == 1):
                but[i].bind(on_press=self.trans_to_hindi)
            if (i == 3):
                but[i].bind(on_press=self.trans_to_english)
        #
        return self.main_layout

    def detectLanguage(self, instance):
        try:
            self.clear(self.my_widget)
        except:
            self.my_widget

        self.text_ = self.s_text.text
        try:
            anser = detect.detect(self.text_)
            result = Language.make(language=anser).display_name()
            self.s_detect = "Translated text is in: " + result
            self.my_widget = Label(text=self.s_detect, )
            self.main_layout.add_widget(self.my_widget)
        except:
            self.text_

    def text_to_speech(self, instance):
        try:
            self.clear(self.my_widget)
        except:
            self.my_widget
        self.text_ = self.s_text.text
        tts_engine = pyttsx3.init()
        tts_engine.say(self.text_)
        tts_engine.setProperty("rate", 50)
        tts_engine.runAndWait()

    def trans_to_hindi(self, instance):
        try:
            self.clear(self.my_widget)
        except:
            self.my_widget
        self.text_ = self.s_text.text
        try:
            transH = GoogleTranslator(target='hi')
            ans = transH.translate(self.text_)
            self.s_detect = "Translated text is: " + ans
            self.my_widget = Label(text=self.s_detect, font_name="Mangal")
            self.main_layout.add_widget(self.my_widget)
        except:
            self.text_

    def trans_to_english(self, instance):
        try:
            self.clear(self.my_widget)
        except:
            self.my_widget
        self.text_ = self.s_text.text
        try:
            trans = GoogleTranslator(target='en')
            ans = trans.translate(self.text_)
            self.s_detect = "translated text is: " + ans
            self.my_widget = Label(text=self.s_detect)
            self.main_layout.add_widget(self.my_widget)
        except:
            self.text_

    def font_name(self,argument):
        in_put = self.insert.text
        match in_put:
            case "1":
                self.s_text.font_name = "Nirmala"
            case "2":
                self.s_text.font_name = "msgothic.ttc"

            case "3":
                self.s_text.font_name = "Segoeui"

            case "4":
                self.s_text.font_name = "malgun"

    def selct_font(self, instance):
        try:
            self.main_layout.remove_widget(self.button)
        except:
            self.button
        try:
            self.main_layout.remove_widget(self.insert)
        except:
            self.insert
        try:
            self.main_layout.remove_widget(self.i_lable)
        except:
            self.i_lable
        self.insert = TextInput()
        self.i_lable = Label(
            text="Enter 1 for Hindi,Gujrati,Gurumukhi,Tamil,Kannad,Malyalam, odia,Telgu\n Enter 2 for Japnees\n Enter 3 for Latin, Greek,Arbik\n Enter 4 for Korian ")
        self.main_layout.add_widget(self.i_lable)
        self.main_layout.add_widget(self.insert)
        self.button = Button(
            text="Set F", font_size=30, background_color="gray",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        self.main_layout.add_widget(self.button)
        self.button.bind(on_press=self.font_name)

    def clear(self, instance):

        try:
            self.main_layout.remove_widget(self.my_widget)
        except:
            self.my_widget
        try:
            self.main_layout.remove_widget(self.button)
        except:
            self.button
        try:
            self.main_layout.remove_widget(self.insert)
        except:
            self.insert
        try:
            self.main_layout.remove_widget(self.i_lable)
        except:
            self.i_lable


if __name__ == "__main__":
    app = MainApp()
    app.run()
