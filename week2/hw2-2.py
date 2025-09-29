def insert(arr, num):
    for i in range (len(arr)):
        if arr[i] > num:
            arr.insert(i, num)
            return
    arr.append(num)


try:
    arr = []
    while True:
        num = int(input())
        insert(arr, num)
        if len(arr) % 2 == 0:
            print((arr[len(arr)//2-1] + arr[len(arr)//2]) // 2)
        else:
            print(arr[len(arr)//2])       
except EOFError:
    pass