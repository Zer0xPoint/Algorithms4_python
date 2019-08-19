from algs4.Stack import Stack

test_str = '( ( 1 + 2 ) * ( ( 3 - 4 ) * ( 5 - 6 ) ) )'
# test_str = '2 * 3 / ( 2 - 1 ) + 3 * ( 4 - 1 )'
test_str_list = test_str.split()
operator_stack = Stack()
numeric_stack = Stack()
operator_count = 0
number_count = 0
operator_precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
res_str = ''


def not_greater(this, peek):
    try:
        a = operator_precedence[this]
        b = operator_precedence[peek]
        return True if a <= b else False
    except KeyError:
        return False


for i in test_str_list:
    if i.isnumeric():
        res_str += i + ' '
    elif i == '(':
        operator_stack.push(i)
    elif i == ')':
        while not operator_stack.is_empty() and operator_stack.peek() != '(':
            res_str += operator_stack.pop() + ' '
        operator_stack.pop()
    else:
        while not operator_stack.is_empty() and not_greater(i, operator_stack.peek()):
            res_str += operator_stack.pop() + ' '
        operator_stack.push(i)
while not operator_stack.is_empty():
    res_str += operator_stack.pop()

print(res_str)
