# all python files have a  varible in the name of "__name__" and its value is : "__main__"
from secend import sayname2
from third import sayname3
# but when we import a pythin file(module) the __name__ changes to :file name 
# for example when we import secend module hes __name__ chanegs to secend and that is the file name 
# note : when we import a module in first all command in module is run 
def sayname1() : 
    print(f"the __name__ in first.py is {__name__}")

sayname1()
sayname2()
sayname3()