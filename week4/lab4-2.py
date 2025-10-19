def solve2(cola):
    """Calculate the total cola after exchanges."""
    print(cola + cola//2)

def solve(bottle):
    """recursively calculate additional colas from bottle exchanges."""
    if bottle == 2:
        return 1
    if bottle < 2:
        return 0
    return bottle // 3 + solve(bottle // 3 + bottle % 3)

while True:
    try:
        cola = int(input())
        print(cola + solve(cola))
    except (EOFError, KeyboardInterrupt):
        break