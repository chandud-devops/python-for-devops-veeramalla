a = 10
b = 5 # globale scope variable

def addition():
    c = 10 # local scope vairable
    print(a + b + c)
    
def sub():
    print(a + b)
addition()
sub()