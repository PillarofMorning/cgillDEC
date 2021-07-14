import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import datetime
from datetime import date
from datetime import timedelta
from kivy.lang import Builder

Builder.load_file('my.kv')


class MyGridLayout(Widget):
    today = date.today()

    def expiration(self, till_expiration):
        return self.today + timedelta(days=till_expiration)

    def datestdtojd(self, stddate):
        fmt = '%Y-%m-%d'
        sdtdate = datetime.datetime.strptime(stddate, fmt)
        sdtdate = sdtdate.timetuple()
        jdate = sdtdate.tm_yday
        return (jdate)



    def callback(self, instance):
        name = self.ids.name_input.text
        self.ids.name_label.text ="todays date:\n " + str(self.today) + "  julian date: " + str(self.datestdtojd(str(self.today))) \
                               + "\n\n70 days from now it will be:\n " + str(self.expiration(70)) + "  julian date: " + str(self.datestdtojd(str(self.expiration(70)))) \
                               + "\n\n60 days from now it will be:\n " + str( self.expiration(60)) + "  julian date: " + str(self.datestdtojd(str(self.expiration(60)))) \
                               + "\n\n55 days from now it will be:\n " + str(self.expiration(55)) + "  julian date: " + str(self.datestdtojd(str(self.expiration(55))))

        if name:
            self.ids.name_label.text = "todays date: " + str(self.today) + "  julian date: " + str(self.datestdtojd(str(self.today))) \
                             + "\n" + str(name) + " days from now it will be: " + str(self.expiration(int(name))) + \
                             " julian date: " + str(self.datestdtojd(str(self.expiration(int(name)))))
        else:
            self.ids.name_label.text = "please enter a valid expiration limit"


class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()