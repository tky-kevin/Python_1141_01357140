def can_arrange(n, target):
    stack = []
    current = 1
    for t in target:
        while current <= n and (not stack or stack[-1] != t):
            stack.append(current)
            current += 1
        if stack and stack[-1] == t:
            stack.pop()
        else:
            return False
    return True

# 12345 -> 23415
# 12-23-34-4-15-5


n = int(input())
if n <= 0:
    exit()

while True:
    target = list(map(int, input().split()))
    if target[0] == 0:
        exit()
    print("YES" if can_arrange(n, target) else "NO")

