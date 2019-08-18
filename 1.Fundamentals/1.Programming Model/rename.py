import os

for file in os.listdir('.'):  # 重命名
    if file[:4] == '1.1.':
        print(file[4:])
        os.rename(file, file[4:])
