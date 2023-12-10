n = int(input())
dictionary = {}
while n != 0:
    query = list(input().split())
    n -= 1
    dictionary[query[0]] = query[1::1]
print(dictionary)
nN = int(input())
while nN != 0:
    nN -= 1
    command, name = input().split()
    if command == "read":
        command = "R"
    elif command == "write":
        command = "W"
    elif command == "execute":
        command = "X"
    if command in dictionary[name]:
        print("OK")
    else:
        print("Access denied")