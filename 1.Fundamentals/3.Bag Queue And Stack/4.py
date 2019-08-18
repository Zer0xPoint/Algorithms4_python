from algs4.Stack import Stack

test_str1 = '[()]{}{[()()]()}'
test_str2 = '[(])'
right_parenthesis = ['(', '[', '{']
left_parenthesis = [')', ']', '}']


def parentheses(test_str):
    s = Stack()
    for i in test_str:
        if i in right_parenthesis:
            s.push(i)
        else:
            pop = s.pop()
            if not ord(pop) - ord(i) <= 2:  # 比较ascii数值，小于等于2的话就是匹配的左括号
                return False
    return s.is_empty()


print(parentheses(test_str2))
