from algs4.Stack import Stack

test_str = '1 + 2 ) * 3 - 4 ) * 5 - 6 ) ) )'
test_str_list = test_str.split()
res_stack = Stack()
num_count = 0
operator_count = 0
for i in test_str_list[::-1]:
    res_stack.push(i)
    if i.isnumeric():
        num_count += 1
        if num_count == 2:
            num_count = 0
            for j in range(operator_count):
                res_stack.push('(')
            operator_count = 0
    elif i is not ')' and i is not ' ':
        operator_count += 1

res_str = ''
for i in res_stack:
    res_str += i + ' '
print(res_str)
