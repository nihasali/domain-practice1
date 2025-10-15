# def decorator(alpha):
#     def wrapper(name):
#         name = name[0] + name[1].upper() + name[2:]
#         print(name)

#     return wrapper

# @decorator
# def func(name):
#     return name

# func('nihas')


# def decorator(alpha):
#     def wrapper(name):
#         print('good morning')
#         print(f'hello {name.upper()}')
#         print('have a nice day')

#     return wrapper

# @decorator
# def func(name):
#     return name

# func('messi')


# def decorator(alpha):
#     def wrapper(num):
#         alpha(num**2)

#     return wrapper

# @decorator
# def func(num):
#     print(num)

# func(3)


def decorator(alpha):
    def wrapper(a,b):
        result=alpha(a,b)
        print(result)
        print(result**2)

    return wrapper

@decorator
def func(a,b):
    return a+b

func(2,4)