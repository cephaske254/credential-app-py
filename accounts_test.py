import unittest
from user_accounts import userAccounts


class AccountsTest(unittest.TestCase):
    '''
    Class that performs testing of the various functions of accounts.py
    '''

    def setUp(self):
        self.new_account = userAccounts(
            'instagram', 'cephaske254', 'test@mail.com', 'admin')

    def tearDown(self):
        userAccounts.accounts = []

    def test_init(self):
        self.assertEqual(self.new_account.platform, 'instagram')
        self.assertEqual(self.new_account.username, 'cephaske254')
        self.assertEqual(self.new_account.password, 'admin')
        self.assertEqual(self.new_account.password, 'admin')

    def test_add_account(self):
        '''
        test case that checks if user accounts are being added to the accounts list
        '''
        userAccounts.add_account(self.new_account)
        self.assertEqual(len(userAccounts.accounts), 1)

    def test_account_exist(self):
        '''
        test case that checks if an account is already registered. If it is registered, it returns the account
        '''
        userAccounts.add_account(self.new_account)
        self.assertTrue(userAccounts.account_exist('instagram', 'cephaske254'))

    def test_get_account(self):
        '''
        test case that checks if an account is already registered. If it is registered, it returns the account
        '''
        userAccounts.add_account(self.new_account)
        get_account = userAccounts.get_account('instagram', 'cephaske254')
        self.assertEqual(get_account.username,'cephaske254')
        self.assertEqual(get_account.email,'test@mail.com')


if __name__ == '__main__':
    unittest.main()
