def rank(key, list_a):
    lo = 0
    hi = len(list_a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if list_a[mid] < key:
            lo = mid + 1
        elif list_a[mid] > key:
            hi = mid - 1
        else:
            for i in reversed(range(mid)):
                if list_a[i] == key:
                    continue
                return i + 1
            return mid


def count(key, list_a):
    lo = 0
    hi = len(list_a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if list_a[mid] < key:
            lo = mid + 1
        elif list_a[mid] > key:
            hi = mid - 1
        else:
            count_num = 0
            for i in reversed(range(mid)):
                if list_a[i] == key:
                    count_num += 1
                    continue
            for j in range(mid, len(list_a)):
                if list_a[j] != key:
                    continue
                count_num += 1
            return mid


def main():
    list_a = [1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 8, 9]
    key = 5
    print(rank(key, list_a))
    print(count(key, list_a))


if __name__ == '__main__':
    main()
