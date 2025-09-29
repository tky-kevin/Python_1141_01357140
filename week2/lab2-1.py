height = int(input())
if height <= 0:
    print("輸入錯誤")
else:
    digits = len(str(height * (height + 1) // 2))
    count = 1
    for i in range(1, height+1):
        j = 0
        while j < i:
            print(f'{count:>{digits}}', end=' ')
            count += 1
            j += 1
        print()