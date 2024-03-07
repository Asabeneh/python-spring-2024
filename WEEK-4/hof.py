# Higher order function: function that take another function as a parameter
# Higher order funcition: function that return another function




def make_square(n):
    return n ** 2

print(make_square(2))
print(make_square(3))

def make_cube(fn, n):
    return fn(n) * n

print(make_cube(make_square, 2))
print(make_cube(make_square, 3))

""" def do_math (n):
    def add_ten():
        return n  + 10
    def multiply_by_ten():
        return n * 10
    return add_ten, multiply_by_ten
    

print(do_math(90)[0]())
print(do_math(90)[1]()) """



def do_math (n):
    def add_ten():
        return n  + 10
    def multiply_by_ten():
        return n * 10
    def subtract_ten():
        return n - 10
    def divide_by_ten():
        return n / 10
    return {
        'add_ten':add_ten,
        'multiply_by_ten':multiply_by_ten,
        'subtract_ten':subtract_ten,
        'divide_by_ten':divide_by_ten
    }
    
print(do_math(90))
print(do_math(90)['add_ten']())
print(do_math(90)['multiply_by_ten']())



