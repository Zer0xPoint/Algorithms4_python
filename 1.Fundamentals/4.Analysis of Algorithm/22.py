# 仅用加减实现的二分查找
# 用斐波那契数列代替二分法求中值
import random

N = 100
target = 23
list_a = list(set([random.randint(0, N) for i in range(N)]))
print(list_a)
fibonacci_list = [1, 1]
while sum(fibonacci_list) < len(list_a):
    fibonacci_list[0] += fibonacci_list[1]  # F(k-1)
    fibonacci_list[1] += fibonacci_list[0]  # F(k)
    print(fibonacci_list[0], fibonacci_list[1])
fk = fibonacci_list[-1]
fk_1 = fibonacci_list[-2]
fk_2 = fk - fk_1
lo = 0
hi = len(list_a)

# 将lo + fk_2作为常规二分查找的mid看待
# 先判断lo + fk_2的位置上相比较target的大小
# p + fk_2能够把list_a分成约1:0.614的两个部分
# 若target较大，则说明mid上的值太小，将lo + fk_2 + 1赋值给lo 使下次循环访问有序数组中较大的那一半
# 反之将lo + fk_2 赋值给hi 使下次循环访问有序数组中较小的那一半
# 每进行一次循环 都将更新一次斐波那契数列的值
while lo < hi and lo + fk_2 < len(list_a):
    if list_a[lo + fk_2] == target:
        print('find', lo + fk_2)
        break
    elif list_a[lo + fk_2] > target:
        hi = lo + fk_2

    else:
        lo = lo + fk_2 + 1

    fk = fk_1
    fk_1 = fk_2
    fk_2 = fk - fk_1
