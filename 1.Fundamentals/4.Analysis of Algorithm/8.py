random_num_list = list(map(int, open('random_numbers').readline().strip().split(',')))
random_num_list.sort()
count = 0
i = 0
while i < len(random_num_list) - 1:
    current_number = random_num_list[i]
    while current_number == random_num_list[i + 1]:
        i += 1
        count += 1
        print(current_number)
        break
    i += 1
print(count)
