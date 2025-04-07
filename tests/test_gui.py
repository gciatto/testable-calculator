import os ; os.environ["KIVY_NO_ARGS"] = "1" # hack for making tests loadable in VS Code
import unittest
from calculator.ui.gui import CalculatorApp


class CalculatorGUITestCase(unittest.TestCase):
    def setUp(self):
        self.app = CalculatorApp()
        self.app._run_prepare()

    def press_button(self, button_text):
        button = self.app.find_button_by(button_text)
        if button is None:
            raise AssertionError(f"Missing button: {button_text}")
        button.trigger_action()

    def assert_button_exists(self, button_text):
        btn = self.app.find_button_by(button_text)
        self.assertIsNotNone(btn)

    def assert_display(self, value):
        self.assertEqual(self.app.display.text, value)   

    def tearDown(self):
        self.app.stop()


class TestLayout(CalculatorGUITestCase):

    BUTTONS_TO_TEST = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 
                       "+", "-", "*", "/", ".", "C", "=", "(", ")", "√", "^"]

    def test_all_buttons_are_there(self):
        for button_text in self.BUTTONS_TO_TEST:
            with self.subTest(button=button_text):
                self.assert_button_exists(button_text)


class TestExpressions(CalculatorGUITestCase):
    def test_integer_expression(self):
        self.press_button("1")
        self.press_button("+")
        self.press_button("2")
        self.assert_display("1+2")
        self.press_button("=")
        self.assert_display("3")

    def test_float_expression(self):
        self.press_button("1")
        self.press_button(".")
        self.press_button("2")
        self.press_button("+")
        self.press_button("2")
        self.assert_display("1.2+2")
        self.press_button("=")
        self.assert_display("3.2")

    def test_complex_expressions(self):
        # test that (1+2)*3 == 9
        self.press_button("(")
        self.assert_display("(")
        self.press_button("1")
        self.assert_display("(1")
        self.press_button("+")
        self.assert_display("(1+")
        self.press_button("2")
        self.press_button(")")
        self.press_button("*")
        self.press_button("3")
        self.assert_display("(1+2)*3")
        self.press_button("=")
        self.assert_display("9")

    def test_sqrt_expression(self):
        # √(5 - 1) + 1 == 3
        self.press_button("√")
        self.assert_display("√(")
        self.press_button("5")
        self.press_button("-")
        self.press_button("1")
        self.press_button(")")
        self.press_button("+")
        self.press_button("1")
        self.assert_display("√(5-1)+1")
        self.press_button("=")
        self.assert_display("3.0")

    def test_power_expression(self):
        # (4 / 2) ^ (5 - 1) == 16
        self.press_button("(")
        self.press_button("4")
        self.press_button("/")
        self.press_button("2")
        self.press_button(")")
        self.assert_display("(4/2)")
        self.press_button("^") # ^ is the symbol for power that we wanna have in our GUI
        self.press_button("(")
        self.press_button("5")
        self.press_button("-")
        self.press_button("1")
        self.press_button(")")
        self.assert_display("(4/2)^(5-1)")
        self.press_button("=")
        self.assert_display("16")
