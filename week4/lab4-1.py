while True:
    n1, n2 = input().split()
    if n1 == '0' and n2 == '0':
        break
    if len(n1) < len(n2):
        n1 = (len(n2) - len(n1)) * '0' + n1
    else:
        n2 = (len(n1) - len(n2)) * '0' + n2
    carry = 0
    carry_count = 0
    for i in range(len(n1)-1, -1, -1):
        if carry + int(n1[i]) + int(n2[i]) >= 10:
            carry = 1
            carry_count += 1
        else:
            carry = 0
    
    if carry_count == 0:
        print("No carry operation.")
    else:
        print(f"{carry_count} carry operation{'s' if carry_count > 1 else ''}.")
