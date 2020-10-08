from kivy.app import App
from kivy.lang import Builder
MILES_TO_KM_EQUATION = 1.60934

class ConvertMilesKmDemo(App):
    def build(self):
        self.title = 'Convert Miles '
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def error_check_input(self):
        try:
            miles_input = float(self.root.ids.get_input.text)
            return miles_input
        except ValueError:
            return 0

    def change_value(self, value):
        miles_input = self.error_check_input() + value
        self.root.ids.get_input.text = str(miles_input)
        self.calculate_input()

    def calculate_input(self):
        miles_input = self.error_check_input()
        conversion_to_km = miles_input * MILES_TO_KM_EQUATION
        self.root.ids.output_label.text = str(conversion_to_km)




ConvertMilesKmDemo().run()