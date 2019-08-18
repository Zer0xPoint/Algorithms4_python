from algs4.Stack import Stack

postfix_str = '1 2 + 3 4 - 5 6 - * *'
postfix_str_list = postfix_str.split()
numeric_stack = Stack()
operator_stack = Stack()

for i in postfix_str_list:
    if i.isnumeric():
        numeric_stack.push(i)
    else:
        res = 0
        num2 = int(numeric_stack.pop())
        num1 = int(numeric_stack.pop())
        if i == '+':
            res += num1 + num2
        elif i == '-':
            res += num1 - num2
        elif i == '*':
            res += num1 * num2
        elif i == '/':
            res += num1 / num2
        numeric_stack.push(res)

print(numeric_stack.peek())
