import random
import string
import pyperclip


class userAccounts:
    '''
    Class that stores user accounts and credentials
    '''
    accounts = []

    def __init__(self, platform, username, password):
        '''
        this function allows users to store their various account details
            Args: platform,username,password
        '''
        self.platform = platform
        self.username = username
        self.password = password

    def add_account(self):
        '''
        this function adds accounts to the accounts list
        '''
        self.accounts.append(self)

    def random_password(length, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(length))

    @classmethod
    def account_exist(cls, platform, username):
        for account in cls.accounts:
            if account.username == username and account.platform == platform:
                return True
            return False

    @classmethod
    def get_account(cls, platform, username):
        '''
        this function searchs for an existing account relative to its username and the platform given
        '''
        for account in cls.accounts:
            if account.username == username and account.platform == platform:
                return account

    @classmethod
    def list_all_credentials(cls):
        '''
        function that allows users to view their account details
        '''
        for user in cls.user_info:
            print(f'Usename: {user.username} password: {user.password}')

    @classmethod
    def copy_password(cls, username, platform):
        for account in cls.accounts:
            if account.username == username and account.platform == platform:
                return pyperclip.copy(account.password)
