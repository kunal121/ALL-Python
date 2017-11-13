'''
=>required
=>keyword
=>variable length
=>default
=> local vs global
'''
#required
def abc(str1):
    print str1
abc('hello')

#keyword
def abc(str1,str2='kunal'):
    print str1,str2
abc(str2='hello',str1='kunal')

#default arguments
def abc(str1="hello",str2='hi'):
    print str1,str2
abc()

#variable length arguments
def abc(*args):
    for i in args:
        print i
abc(1,2,3,4)

#global vs local
total=0
def abc():
     global total
     total =34
abc()
print total
