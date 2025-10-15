
#---------------------------------------------------------------------------- using random -------------------------------------------------------------------

# list1 = ['apple','orange','peanut','banana','tomato']
# import random
# random.shuffle(list1)
# print(list1)

# shuffled_list=random.sample(list1,len(list1))
# print(shuffled_list)


# import random

# random.seed(10)  # for reproducibility
# print(random.random())          # Random float 0–1
# print(random.randint(1, 100))   # Random integer
# print(random.choice('ABCDE'))   # Random letter
# print(random.sample(range(10), 3))  # Random 3 unique numbers



# -------------------------------------------------------------------------------------------------------------------------------------------------------------

# def func(num):
#     if num==5:
#         return 'a'

#     else:
#         return 'b'

# print(func(5))


# func1 = lambda num: 'a' if num==5 else 'b'

# print(func1(6))

# ------------------------------------------------------------------------------------

def check_dict_keys_type(d):
    if not d:  # empty dict
        return True  # or raise an exception if you prefer

    key_types = {type(k) for k in d.keys()}  # collect unique types
    if len(key_types) > 1:
        raise TypeError(f"Dictionary keys have different types: {key_types}")
    return True  # all keys have the same type

# Example usage
# my_dict = {1: "a", 2: "b", 3: "c"}
# check_dict_keys_type(my_dict)  # ✅ works fine

my_dict2 = {1: "a", "two": "b"}
check_dict_keys_type(my_dict2)