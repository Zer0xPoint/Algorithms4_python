def josephus(n, m):
    alive_index_list = [i for i in range(1, n + 1)]
    index = 0
    kill_count = 0
    while len(alive_index_list) - kill_count >= 1:
        if alive_index_list[index] == 0:
            break
        else:
            kill_count += 1
        print(alive_index_list[index], end=' ')
        alive_index_list[index] = 0
        index += m
        if index >= len(alive_index_list):
            index -= len(alive_index_list)


josephus(7, 2)
