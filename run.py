from users import User
import pyperclip
from user_accounts import userAccounts
def new_user_account():
    print('Create New user account')
    usr_firstname = input('Enter First Name: ')
    usr_lastname = input('Enter Last Name: ')
    usr_username = input('Enter Username: ')
    if(User.user_exists(usr_username)):
        print('User already exists')
        new_user_account()
    else:
        usr_password = input('Type your login password: ')
        usr_password1 = input('Confirm your login password: ')
        if usr_password == usr_password1:
            new_User = User(usr_firstname, usr_lastname,usr_username, usr_password)
            User.save_user_info(new_User)
            print(f'{usr_firstname} added as user\n---------')
            login_account()
def login_account():
    print("-------Login-------")
    exists = User.user_login(input('Enter Username: '),input('Enter Password: '))
    if(exists !=True):
        print('Check your password!')
    else:
        acc_short_code = input('Hello, if you want to add an existing platform acccount, type EX. If you want to generate new account details, type NW').lower()
        if(acc_short_code == 'nw'):
            reg_new_platform()
        elif acc_short_code =='ex':
            reg_existing_platform()
        else:
            print('Invalid Option')
            login_account()
def reg_existing_platform():
    ex_platform = input('Enter platform e.g. Facebook,Google, Instagram etc.: ')
    ex_username = input('Enter account username/email: ')
    if(userAccounts.account_exist(ex_platform, ex_username)):
        print(
            'Account on {ex_platform} already registered with username/email {ex_username}')
    else:
        ex_password = input('Enter account password: ')
        new_account = userAccounts(
            ex_platform, ex_username, ex_password)
        # Adding new account if it doesnt exist
        userAccounts.add_account(new_account)
        print(
            f'Account {ex_username} added to platform {ex_platform}')
def reg_new_platform():
    nw_platform = input('Enter platform e.g. Facebook,Google, Instagram etc.: ')
    nw_username = input('Enter account username/email: ')
    nw_password = input('Type password or type AUTO to auto-generate password: ')
    if(nw_password == 'auto' or nw_password == 'AUTO'):
        nw_password = userAccounts.random_password(
            int(input('Enter preferred length: ')))
        print(f'Your password is {nw_password}')
    else:
        if(input('Confirm your password: ') != nw_password):
            print('Passwords didn\'t match')
            main()
    new_account = userAccounts(
        nw_platform, nw_username, nw_password)
    userAccounts.add_account(new_account)
    print(f'Account {nw_username} added to platform {nw_platform}')
    if input('Type CP to copy password').lower() == 'cp':
        pyperclip.copy(nw_password)
        print(f'Password of {nw_username } copied to clipboard')
        if input('Type LS to list all your credentials or press any key to return to main').lower() == 'ls':
            userAccounts.list_all_credentials()
        else:
            login_account()
    reg_new_platform()


def main():
    print('Hello! Welcome to credential manager\nUse CN to create an new user account, or LG to login to an existing user account')
    short_code = input().lower()
    if short_code == 'cn':
        new_user_account()
    elif short_code == 'lg':
        login_account()
    else:
        print('Invalid Option')
        main()
if __name__ == '__main__':
    main()
