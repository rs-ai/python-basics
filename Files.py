f1 = open('/Users/yyz/File.txt','r') #specify the path where the file is present
#r/w/a - read, write or append options

for line in f1:
    print(line)    
f1.close()

f1 = open('/Users/yyz/File.txt','a')
f1.write('\n add this line to the file')
f1.close()
