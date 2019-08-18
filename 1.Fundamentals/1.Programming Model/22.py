def rank(key, a, lo, hi, depth):
    print(' ' * depth, end='')  # 输出空格不换行
    print(lo, hi)
    depth += 1  # 记录深度
    if lo > hi:
        return -1
    mid = lo + (hi - lo) // 2
    if key < a[mid]:
        return rank(key, a, lo, mid - 1, depth)
    if key > a[mid]:
        return rank(key, a, mid + 1, hi, depth)
    else:
        return mid


def main():
    a = [10, 11, 12, 16, 18, 24, 33, 58, 59, 68, 88, 98, 1]
    a.sort()
    print(a)
    depth = 0
    print(rank(18, a, 0, len(a) - 1, depth))


if __name__ == '__main__':
    main()
