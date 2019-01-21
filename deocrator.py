# # def html_tag(tag):
# #     def wrap(content):
# #         print(f'<{tag}>{content}</{tag}>')
# #     return wrap
# #
# # h1_tag = html_tag('h1')
# # h1_tag("Blog header")
# # h1_tag("Blog subheader")
# #
# # p_tag = html_tag('p')
# # p_tag("A brief history of yo salad ass")
#
#
# def full_decorator(prefix):
#     def outer_func(original_function):
#         def inner_func(*args, **kwargs):
#             print(prefix)
#             original_function(*args, **kwargs)
#         return inner_func
#     return outer_func
#
#
# # @full_decorator('Prefix') # I Passes argument into the first function, creating an enclosing scope variable
# def display(msg):         # Passess function as an argument to the child function
#     print(msg)           # Assigns the name of the original function (display) to the grandchild function of the decorator
#
# decorated_display = full_decorator("Prefix") # II Passes argument into top function creating a varible accessable by its children and grandchildren
# display = decorated_display(display) # II Passes function as argument to the child function, child function returns grand child function assigning it to display
#
#
# # Both methods (I, II) followed the same process
# # The grandchild function will be executed as display() adding extra functionality to the original display function. The original display function will be executed inside the granchild function
# # The grandchild function (inner_func) will have access to the variables assigned or created inside the parent (outer_func) and grandparent functions (full_decorator)
#
#
# # print(display)
# # display("Hello")
#
#
#
#
# def full_decorator(prefix):
#     def semi_decorator(sub_prefix):
#         def outer_func(original_function):
#             def inner_function(*args, **kwargs):
#                 print(prefix)
#                 original_function(*args, **kwargs)
#             return inner_function
#         return outer_func
#     return semi_decorator
#
#
# @full_decorator("Prefix")
# def display(msg):
#     print(msg)
#
# print(display)



class A:
    def __init__(self, obj):
        self.obj = obj


class B:
    def __init__(self, *args):
        self.figures = args


test = B(A(test))

print(test)
