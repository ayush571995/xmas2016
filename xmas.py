from clint.textui import colored
from termcolor import colored
import colors
def trapezium(n,count):
    for j in range(0,7):
        for s in range(45-6*count-j,0,-1):
            print(' ',end='')
        print(colored('ᴧ', 'green'), end='')
        for i in range(0,n):
            print(colored('ᴧ', 'green'), end='')
        print()
        n+=2
    return n
def triangle():
    count=0
    for i in range(0,7):
        for s in range(50-i,0,-1):
            print(' ',end='')
        for j in range(0,count+1):
            print(colored('ᴧ', 'green'), end='')
        print()
        count+=2
def diamond():
    count=1
    for i in range(0,2):
        for s in range(50-i,0,-1):
            print(' ',end='')
        for j in range(0,count):
            print(colored('•','red'),end='')
        print()
        count+=2
    for j in range(50,0,-1):
        print(' ',end='')
    print(colored('•','red'))
diamond()
triangle()
count=0
k=trapezium(10,count)
count+=1
for i in range(1,3):
    l=trapezium(k-3,count)
    k=l
    count+=1
print('\n\n\n')
for i in range(0,20):
    print(' ',end=' ')
with colors.pretty_output(colors.BOLD, colors.FG_RED) as out:
    out.write("❄ MERRY CHRISTMAS ❄\n\n\n\n ")
for i in range(0,20):
    print(' ',end=' ')
with colors.pretty_output(colors.FG_BLUE) as out:
    out.write(" by ayush571995 ⚡")
