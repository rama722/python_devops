print("project xyz azuredevops")


name = "Ramanaidu Guntupalli"
print(name)

# global variable
a = 3
b = 5
def addition():
    print(a + b) 

def sub():
    print(a - b) 

def mul():
    print(a * b) 

addition()
sub()
mul()

# local variable
def addition():
    a = 3
    b = 8
    print(a + b) 

def sub():
    a = 3
    b = 9
    print(a - b) 

def mul():
    a = 3
    b = 6
    print(a * b) 

addition()
sub()
mul()

# local/global varibale 
a = 3
b = 5
def addition():
    c = 10
    print(a + b + c)

addition()