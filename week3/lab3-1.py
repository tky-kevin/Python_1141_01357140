n, m = map(int, input().split())
friends_a = set(map(int, input().split()))
friends_b = set(map(int, input().split()))
common_friends = friends_a & friends_b
print(len(common_friends))
if common_friends:
    print(*sorted(common_friends))