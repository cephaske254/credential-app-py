class User:
    '''
    Class that allows the users to create their login details
    '''
    user_info = []

    def __init__(self, first_name, last_name, username, password, password1):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.password1 = password1

    def save_user_info(self):
        '''
        function that appends user login info
        '''
        self.user_info.append(self)

    
    @classmethod
    def user_exists(cls,username):
        '''
        a class function that checks if a certain user with the inputted username exists and returns true or false
        '''
        for user in cls.user_info:
            if user.username==username:
                return True
        return False

    @classmethod
    def get_user_info(cls,username):
        '''
        function that allows users to view their account details
        '''
        for user in cls.user_info:
            if user.username == username:
                return user
        
    @classmethod
    def user_login(cls,username,password):
        '''
        function that checks if the username of a registered account equals the inputted password
        '''
        if cls.get_user_info(username).password == password:
            return True
        return False