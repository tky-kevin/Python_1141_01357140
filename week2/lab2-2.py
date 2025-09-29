def sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

n = int(input())
if n <= 0:
    print("輸入錯誤")
    exit()
arr = list(map(int, input().split()))
print('排序前的數列:', ' '.join(map(str, arr)))
sort(arr)
print('排序後的數列:', ' '.join(map(str, arr)))