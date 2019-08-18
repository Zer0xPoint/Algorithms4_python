from algs4.Stack import Stack

test_str_list = '( ( 1 + 2 ) * ( ( 3 - 4 ) * ( 5 - 6 ) ) )'.split()
test_stock = Stack()

for i in test_str_list:
    test_stock.push(i)


def copy(original_stack):
    temp_list = []
    copied_stock = Stack()
    for i in original_stack:
        temp_list.append(i)
    for i in temp_list[::-1]:
        copied_stock.push(i)
    return copied_stock


print(copy(test_stock))
