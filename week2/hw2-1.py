height =  int(input())
if height <= 0:
    print("輸入錯誤")
else:
    for h in range(height-1):
        print(' '*(height-h-1) + '*' + ' '*(2*h-1) + ('*' if h != 0 else ''))
    print('*'*(2*height-1))