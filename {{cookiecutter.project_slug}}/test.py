import unittest
import re


class TestStripe(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestStripe, self).__init__(*args, **kwargs)
        with open('order.html', 'r') as file_descriptor:
            self.dom_str = file_descriptor.read()

    #Check if redirectToCheckout function call is present        
    def test_redirect_to_checkout(self):
        self.assertNotEqual(self.dom_str, '.redirectToCheckout', 'No stripe redirect call found!')
    
    #Check if success_url redirects to order_success.html
    def test_success_url(self):
        self.assertRegex(self.dom_str, r'successUrl: \'https:\/\/[a-z]*\.com/order_success\.html\'', 'No order_success.html redirect found on checkout success.')
    
    #Check if cancel_url redirects to order.html
    def test_cancel_url(self):
        self.assertRegex(self.dom_str, r'cancelUrl: \'https:\/\/[a-z]*\.com/order\.html\'', 'No order.html redirect found on checkout cancel.')


if __name__ == '__main__':
    unittest.main()
