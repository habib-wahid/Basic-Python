def func():
   global p
   p = "awesome"
   print(p)

def Main():

    x = 20
    y = "habib"
    print(x)
    print(y)
    #assigning values
    x,y,z = "orange",20,"red"
    print(x)
    print(y)
    print(z)
    #assigning values together
    x = y = z = "apple"
    print(x+y+x)
    #global variable
    func()
    p = "good"
    print(p)

if __name__=="__main__":
    Main()
