

class users :
    def __init__(self ,  giveName , giveFamily ):
        self.name = giveName
        self.family = giveFamily
    def __repr__(self):
        text = "now we change defult ; "
        text2 = f"{self.name} {self.family}"
        return text+text2

hossein = users('hossein' , 'askari')
print(hossein)
# when we print a instance (نمونه) of class its defult print simething like this : <__main__.users object at 0x0000015F293F5FD0>
# with '__repr__' function we can change the defult



