import os
os.system('clear')
print('Run it by python-3\n')
next =input("\033[91m{}\033[00m" .format('[1/7]hit Enter -> Continue'))


print('\n\n')
print("we have two variables 'a' and 'b' :")
a = 857642747452624645215346576879786725767858769896897847675265452143543645768768974585674363252145467
b = 4874582745533454131835434876543453
print('a=',a)
print('b=',b)
print('\n')
next =input("\033[91m{}\033[00m" .format('[2/7]hit Enter -> Continue'))
print('\n\n')

print('Now -> c = a * b')
c = a * b
print('c=',c)
print('\n')
next =input("\033[91m{}\033[00m" .format('[3/7]hit Enter -> Continue'))

print('\n\n')
print("OK, we know 'c / b' shoud equal 'a' but python3 says:")
print('c/b =>',c/b)
print("check this number by this way: '( c / b ) == a' ")
print('(c/b)==a\n>>',(c/b)==a,'\n')
print('\n')
next =input("\033[91m{}\033[00m" .format('[4/7]hit Enter -> Continue'))

print('\n\n')
print("also '(c/b)' is not equal 'a' even though we convert it to 'int'")
print('int(c/b)=',int(c/b))
print('check it:')
print('int(c/b)==a\n',(c/b)==a)
print('\n')
next =input("\033[91m{}\033[00m" .format('[5/7]hit Enter -> Continue'))

print('\n\n')
print("'x = int(c/b)' i will show you resualt of a-x:")
x = int(c/b)
print('a-x')
print('>> ',a-x)
print("'a' is so bigger than 'x'")
print('\n')
next =input("\033[91m{}\033[00m" .format('[6/7]hit Enter -> Continue'))

print('\n\n')
print('this is a bug! it is not? i discovered it  7-jun-2019')
print('but in python 2 we have not this problem.')
print("\033[91m{}\033[00m" .format('My Github & Twitter'))
print('Github.com/pyc21t')
print('Twitter.com/pyc21t')
print('\n')
next =input("\033[91m{}\033[00m" .format('[7/7]hit Enter -> Exit'))
