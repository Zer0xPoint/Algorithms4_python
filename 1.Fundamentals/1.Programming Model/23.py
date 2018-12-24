def rank(key, a, lo, hi):
    if lo > hi:
        return -1
    mid = lo + (hi - lo) // 2
    if key < a[mid]:
        return rank(key, a, lo, mid - 1)
    if key > a[mid]:
        return rank(key, a, mid + 1, hi)
    else:
        return mid


def main():
    data_w_name = 'tinyW.txt'
    data_t_name = 'tinyT.txt'
    data_w = []
    with open(data_w_name, 'r') as f:
        for line in f:
            line = int(line.strip())
            data_w.append(line)
    data_w.sort()
    is_exist = []
    not_exist = []
    with open(data_t_name, 'r') as f:
        for line in f:
            line = int(line.strip())
            if rank(line, data_w, 0, len(data_w) - 1) != -1:
                is_exist.append(line)
            else:
                not_exist.append(line)
    print(is_exist)
    print(not_exist)


if __name__ == '__main__':
    main()
