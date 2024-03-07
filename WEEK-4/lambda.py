# Anonyomous - A function without name

make_square = lambda x : x ** 2

print(make_square(10))

# x^2 + 6x + 9 => -3

value = lambda x: x ** 2 + 6 * x + 9
print(value(-3))

# x = 2, y = 4, z = -3
sol = lambda x, y, z : 2 * x ** 2 + 2 * x * y * z + y ** 2 + z ** 2
print(sol(2, 4, -3))

# ax + by = c
# 4x + 6y = 10
# x = 2, y = 4
# find ? 4x + 6y - 10

value = lambda x, y : 4 * x + 6 * y - 10
print(value(2, 4))






