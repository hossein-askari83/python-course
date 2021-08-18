 
import translators as ts 

englishText = "i will learn python in two month"
print(ts.bing(englishText,from_language='en' , to_language='fa'))
help(ts)
# for more information go to part 52 of studing python by maste ordookhani

print("----------------------------------")

import pyfiglet as pf
text = pf.figlet_format("hossein")
print(text)