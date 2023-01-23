
# Note:  Closure in python is a function object. 
#        Closure is a function that behavies like an object
#        Closure is a inner function
'''
    <Closure>

    In this code, the variable 'message' is declared in the higher scope and the inner function can access it.
    The inner_func is the closure and it will be returned as an object to the parent function that is the (outer) outer_fun

    < Non-Local Variables in Nested Functions>

    Every variable is in a certain scope, in closure the variable has both scopes the parent function (outer) and the inner function
    Message can be seen by both functions
'''
def outer_fun(): # the outher function
    message = "Hello"
    def inner_func():
        print(message)
    return inner_func

executa =  outer_fun()
#print(" will print the object function outer_fun ", executa)
executa()

'''
   < Non-Local Variables in Nested Functions>

    Python creates a second register in memory for the inner scope variable and points to the parent scope variable
    outer_scope and inner_scope were created just to test, representing  the scope of each function
'''

def divider(y):
    outer_scope = y
    def divide(x):
        inner_scope = x
        return inner_scope / outer_scope
    
    return divide

# outer function is instanciated passing the y parameter
d1 = divider(2)
#print(" will print the object function divider ", d1)
# outer function is called passing the inner function parameter
executa = d1(8)
# Lets print the result 8 / 2
print(executa)

'''
    another example ...
'''

def f1(operator1):
    def f2(operator2):
        return operator1 + operator2
    
    return f2
# instanciate the parent function with the first operator. It is only an object function so far
soma = f1(10)
#print(" will print the object function f1 ", soma)
# execute the closure and call the inner function with the second operator 
executa = soma(2)
# lets print the sum of 10 + 2
print(executa)


'''
    another example ..
'''
def full_message(start):
    start = start+"BLA BLA"
    def internal_message(end):
        return f'{start}{end}'
    return internal_message

# instanciate an object to the full message
message = full_message("This is the OUTHER function - ")
# call the inner function to closure the function
executa = message("I am the INNER function message")
# lets see the full message
print(executa)


'''
    Challenge:
    1 ) Python closure cannot assign variables declared in outer scope. 
    Found cannot be assigned within helper because it becames a local variable and hides the found in outer(enclosing) scope
    R. use a nonlocal found variable to bind the inner function to an external scope variable
'''
controls_id = [5000, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009]
reserved_id = {5009, 5003}

def display_sorted_control(control, reserved):
    found = False
    def inner_function(id):
        if id in reserved:
             # The following line is required to refer to outer's function
            nonlocal found
            found = True
            return (0, id) # return 0 to sort function
    
        return (1, id) # return 1 to sort function
    control.sort(key=inner_function)
    # print(control)
    return found

executed = display_sorted_control(controls_id, reserved_id)
print(executed)


"""
    Note that the x is assigned in the outer scope with 1
    2 + 1 = 3
"""
def func1():# outer function
    x = 1 # variable defined in outer scope
    def func2(a):# inner function
        print(a + x) # able to acces the variable of outer function x
    func2(2) # call inner func
# call outer function
func1()

'''
    Now note that inside the inner function the variable x is assigned with 4 and hide the previous one
    2 + 4 = 6
'''
def func1():# outer function
    x = 1 # variable defined in outer scope
    def func2(a):# inner function
        x = 4
        print(a + x) # able to acces the variable of outer function x
    func2(2) # call inner func
# call outer function
func1()

'''
    To access or change variables within a nested function (inner func) 
    1) make the variable an iterable
    2) use nonLocal class. The nonlocal statement causes the listed identifiers to refer to previously bound variables in the nearest enclosing scope excluding globals
'''

def func1_iterable():
    x = [1, 5]
    def func2_iterable(a):
        x[0] = a
    func2_iterable(2)
func1_iterable()

def outer_func2():
    found = False
    def inner_func2(y):
        nonlocal found
        if y == 2:
            found= True
    inner_func2(2)
    return found

resultado = outer_func2()
print(resultado)

'''
    fibonacci formula
'''
def fibonacci(first, limit):
    somados = first
    elements= [first]
    def soma(before): 
        nonlocal somados
        if somados >= limit:
            return somados
        else:
            next =somados
            somados = somados + before
            elements.append(somados)
            soma(next)
    soma(first)
    print("Total Sum", somados)

    return somados

fibonacci(1,33)
