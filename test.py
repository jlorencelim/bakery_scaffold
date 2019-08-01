import unittest

class TestStripe(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestStripe, self).__init__(*args, **kwargs)
        with open('order.html', 'r') as file_descriptor:
            self.dom_str = file_descriptor.read()
        
    def test_stripe_script_elem(self):
        stripe_script_index = self.dom_str.index('https://js.stripe.com/v3')        
        self.assertNotEqual(stripe_script_index, -1)

    def test_checkout_button(self):
        button_elem_index = self.dom_str.index('id="btn-checkout"')
        self.assertNotEqual(button_elem_index, -1)
    
    def test_input_elem(self):
        input_elem_index = self.dom_str.index('type="text')
        self.assertNotEqual(input_elem_index, -1)

if __name__ == '__main__':
    unittest.main()