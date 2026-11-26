n = int(input("введите количество людей: "))
users = dict()
for i in range(n):
    line = input("имя, товар, количество: ").split(" ")
    print(line)
    if line[0] in users:
        users[line[0]][line[1]] = line[2]
    else:
        users[line[0]]= {line[1]: line[2]}
for key, value in users.items():
    print(f"{key}")
    for key2, value2 in users[key].items():
        print(f"{key2} {value2}")
