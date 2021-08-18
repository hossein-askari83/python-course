# we have a few ways naming attribute in class :
# 1  = _name
# 2  = __name
# 3  = __name__

class user :
    def __init__(self , getUserName , getPass,getNationalCode):
        self.user_name = getUserName # --> normal naming
        self._password = getPass # --> this is a pravate attribute BUT  we no have any pravate value in python but it some how pravate
        self.__nationalCode = getNationalCode # --> when we give a name like this to attribute we dont have access to it with this name and his name is change to '_user__nationalCode'
        # and we call this way naming : name mangling
        self.__example__ = "this is normal just special naming" # --> this is a special naming like some name : PI , int , class , print :
        # these names are special nemes and we cant use them for naming our values and __example__ just like this but we can use it to naming our values

user1 = user("ali77" , "ali77@gmail.com" , 1123123132)
print(user1.user_name)
print(user1._password)
# print(user1.__nationalCode)  # - - - - > this code give us error couse we dont have  access to __nationalCode
print(dir(user1)) # dir  = this fuction give us attribute that we write that in it
print(user1._user__nationalCode) # now we have access to this attribute and we can print it
print(user1.__example__)
# BIG NOTE = IN THIS ATTRIBUTE NAMING : __NAME , WE CALL IT NAME MANGLING
# SO :
# 1  = _name  === > pravate (not actully)
# 2  = __name === > secret or dont have access
# 3  = __name__ === > special name ( key name)
