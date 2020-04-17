import unittest
from users import User


class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User('cephas', 'too', 'cephaske254', 'admin', 'admin')

    def tearDown(self):
        User.user_info =[]

    def test_init(self):
        '''
        function to test for initialization of variables
        '''
        self.assertEqual(self.new_user.first_name, 'cephas')
        self.assertEqual(self.new_user.last_name, 'too')
        self.assertEqual(self.new_user.username, 'cephaske254')
        self.assertEqual(self.new_user.password, 'admin')
        self.assertEqual(self.new_user.password1, 'admin')
    def test_save_user_info(self):
        '''
        Function that checks if user credentials are being saved
        '''
        User.save_user_info(self.new_user)
        self.assertEqual(len(User.user_info),1)
    def test_user_exists(self):
        '''
        a test function that returns true or false to check if a certain user exists
        '''
        User.save_user_info(self.new_user)
        self.assertTrue(User.user_exists('cephaske254'))
    def test_get_user_info(self):
        '''
        function that allows the user to view their account details
        '''
        User.save_user_info(self.new_user)
        self.assertEqual(User.get_user_info('cephaske254'),self.new_user)

    def test_user_login(self):
        User.save_user_info(self.new_user)
        self.assertTrue(User.user_login('cephaske254','admin'))


if __name__ == '__main__':
    unittest.main()
