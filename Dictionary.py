# dictionary has some key value pairs
dict1={}
# if exist then update that value otherwise create a new key
dict1['kunal']='hi'
#
#dict1.clear() clear the values in dictionary
# del dict1 delete the dictionary
'''
dict1.keys()
dict1.items()
dict1.values()
'''
for i in dict1.keys():
    print i
for i in dict1.items():
    print i

print 'kunal' in dict1.keys()
