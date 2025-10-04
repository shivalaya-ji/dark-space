y = 10 #global variable
def inner() :
    x = 4 #local variable
    global y
    y = y+2
    print("x: ", x)
    print("inside the function y: ", y)

inner()
print("y: ", y)
