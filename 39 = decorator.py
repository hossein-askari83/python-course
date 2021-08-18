class user :
  def normalFunction(self):
      print("this is normal function")
      print(self)

      # print("--------------------------------------------------")
  @classmethod
  def functionWithDecorator(cls):
      print("this is function with decorator")
      print(cls)

example = user()


example.normalFunction() # it will return this :  <__main__.user object at 0x0000022B189AAFA0>
print("-------------------------------")
example.functionWithDecorator() # it will return this : <class '__main__.user'>

print("===================================")

user.normalFunction() # it give us error cuze normal functions whant a instance and they dependent on that  instance
print("-------------------------------")
user.functionWithDecorator() # it again print : <class '__main__.user'> cuz decorator do something to founction and they not dependent to
# instance any more and it(function) return to class
