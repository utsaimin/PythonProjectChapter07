try:
    file = open("d:/data.txt", "r")
    sum = 0
    for data in file:
        sum = sum + int(data)
    print(sum)
except ValueError:
    print("Tipe data bukan int")
