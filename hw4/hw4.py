"""
Food
"""

def my_sum(list):
    if not list:
        return 0
    else:
        return sum(list)

def longest_interval(list):
    if len(list) == 1:
        if list[0] > 0:
            print(list, list)
            return list, list # max interval, max interval that ends on that number
        if list[0] <= 0:
            print([], [])
            return [], []
    l1, l2 = longest_interval(list[:-1])
    if my_sum(l1) < my_sum(l2) + list[len(list)-1]:
        l1 = l2 + [list[len(list)-1]]
    if (my_sum(l2)+list[len(list)-1]) < 0:
        l2 = []
    else:
        l2.append(list[len(list)-1])
    print(l1, l2)
    return l1, l2


one = [2, -6, 4, 8, -10, 0, 5, 3]
two = [2, -6, 4, 8, -10, 4]
three= [0,0, -2]
print("Answer: ", longest_interval(one)[0])
