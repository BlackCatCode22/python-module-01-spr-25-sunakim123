print("Hello world!")

x = 15
print(x)

nzt = input('Enter your name: ')
print("Hello",nzt)

xh = input("Enter hours: ")
xr = input("Enter rate: ")
xp = float(xh) * float(xr)
print("Pay:", xp)

aaa = 25
bbb = 5
ccc = aaa * bbb
print(ccc)

ddd = aaa ** bbb
print(ddd)

s = 3
if s > 5:
    print('Bigger than 5')
else:
    print('Smaller than 5')

u = 20
if u < 2:
    print('Small')
elif u < 10:
    print('Medium')
else:
    print('Large')
print('All done')

astr = 'Bob'
try:
    print('Hello')
    istr = int(astr)
    print('There')
except:
    istr = 1
print('Done', istr)
