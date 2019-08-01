import unittest
import re

class TestStripe(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestStripe, self).__init__(*args, **kwargs)
        with open('order.html', 'r') as file_descriptor:
            self.dom_str = file_descriptor.read()

    #Check if stripe script element is present   
    def test_stripe_script_elem(self):
        stripe_script_index = self.dom_str.index('https://js.stripe.com/v3')        
        self.assertNotEqual(stripe_script_index, -1, 'Stripe script element missing')

    #Check if checkout button element is present with provided id
    def test_checkout_button(self):
        button_elem_index = self.dom_str.index('id="btn-checkout"')
        self.assertNotEqual(button_elem_index, -1, 'Checkout Button not found!')
    
    #Check if any HTML input element is present
    def test_input_elem(self):
        #input_elem_index = self.dom_str.index('type="text"')
        self.assertRegex(self.dom_str, r'type="text"|type=\'text\'|type="number"|type=\'number\'', 'No Input Element Found')

    #Check if redirectToCheckout function call is present        
    def test_redirect_to_checkout(self):
        self.assertNotEqual(self.dom_str, '.redirectToCheckout', 'No stripe redirect call found!')
    

    #Check if stripe constructor function call is present   
    def test_stripe_constructor(self):
        self.assertNotEqual(self.dom_str, 'Stripe(', 'Stripe Constructor function call not found!')

if __name__ == '__main__':
    unittest.main()