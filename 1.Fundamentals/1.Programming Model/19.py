def fibonacci(n, fib_list):
    while n:
        fib_list_len = len(fib_list)
        fib_list.append(fib_list[fib_list_len - 1] + fib_list[fib_list_len - 2])
        n -= 1
    return fib_list


fib_list = [1, 1]
print(fibonacci(100, fib_list))
