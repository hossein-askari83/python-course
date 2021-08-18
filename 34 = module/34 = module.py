

# import module ways :
# import random
# from random import randint
# import random as rand
import random as rand
print(rand.randint(1, 10))
courses = ['python', 'html', 'django', 'css']
print(rand.choice(courses))

# in fact the modules are python files and even we can make a module by our selfs : 

import exaple_module_for_part_34 as ex

print(ex.s_circle(21))