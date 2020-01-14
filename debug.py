def wbsu():
    return 6

x = wbsu()
for i in [1, 2, 4, 6, 5]:
    x += i

if x > 23:
    print ("Welcome!")     
print (x)
if x > 23:
    print ("Debugging: debug.py, line 12")
    print ("Welcome! to Hell")