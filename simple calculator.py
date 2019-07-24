# simple calculator
from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

print( Back.GREEN)
print ( Fore.BLUE)
what = input ('Choose an option (-,+):')
print (Back.RED)
print(Fore.WHITE)
a = float (input ('Type the fisrt figure:') )
b = float (input ('Type the second figure:') )


print (Back.CYAN)
print (Fore.WHITE)
if what == '+':
    c= a + b
    print ('Result: '+ str(c))
elif what == '-':
	c = a - b
	print ('Result:' + str(c))

else:
	print('Wrong option is chosen!')

input()