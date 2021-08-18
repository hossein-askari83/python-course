

class users :
    activeUsersCount  = 0
    activeUsersList = []
    allowedUsers = ["ali", "hossein" , "iman" , "javad" , "sara"]
    def __init__(self , userName , userFamily):
        self.name = userName
        self.family = userFamily
    def login(self):
        if self.name not in users.allowedUsers :
            raise ValueError("you cant login")
        print(f"{self.name} is logged in ")
        users.activeUsersCount += 1
        print(f"{users.activeUsersCount} users is active ")
        users.activeUsersList.append(self.name)
        print(f"active users are : {users.activeUsersList}")
    def logout(self):
        print(f"{self.name} is log out ")
        users.activeUsersCount -= 1
        print(f"{users.activeUsersCount} users is  active ")
        users.activeUsersList.remove(self.name)
        print(f"active users are : {users.activeUsersList}")

user1 = users("sara" , "ahamdi")
user2 = users("ali" , "asghari")
user3 = users("asghar" , "rahmati")

user1.login()
user2.login()
# user3.login() # this give us erroe cuz "asghar" is not in allowed users
user1.logout()