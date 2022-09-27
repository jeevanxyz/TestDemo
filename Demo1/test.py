fh=open('C:\\Users\\AG29464\\OneDrive - Anthem\\Desktop\\files\\demo.txt','w')
try:
    for i in range(10):
        fh.write("this is line no %d\n" % (i+1))
finally:
    fh.close()
fh1 = open('C:\\Users\\AG29464\\OneDrive - Anthem\\Desktop\\files\\demo.txt', 'r')
print(fh1.readlines()[4])