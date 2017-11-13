# file handling
# open a file
fo=open("foo.txt","w+")
fo.write("python  is awsome")
fo.close()
# modes in file
a+
r+
rb+
w+
b+
# methods in file
fo.close()
fo.read(10)
fo.tell() #gives position of the pointer
fo.seek(0,0)
fo.closed# file is closed or not
fo.mode
fo.name# give the file name


#os
import os
os.rename('foo.txt',"foo1.txt")
os.remove('foo.txt')
os.mkdir('mkdir_name')
os.getcwd()


