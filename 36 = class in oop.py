
class shape :
    def __init__(self , tolv , arzv): # we use __init__ function to defind attributes
        # we can use any word insted of ' self '
           self.tol = tolv # so now 'tol' is a attribute for shape class
    # to access a attribute in __init__ founction to another function we must use "self.attribute name"
           self.arz = arzv
    def masahat(self ): # to defind functionality in class we defind a function like this
            return f"THE MASAHAT IS : { self.arz * self.tol}"
    def mohit(self):
            return f"THE MOHIT IS  : {(self.tol + self.arz) * 2}"

mostatil = shape(4,7)
print(mostatil.masahat())
print(mostatil.mohit())
