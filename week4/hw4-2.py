class Solution:
    relation = {
        'A': 'A',
        'E': '3',
        'H': 'H',
        'I': 'I',
        'J': 'L',
        'L': 'J',
        'M': 'M',
        'O': 'O',
        'S': '2',
        'T': 'T',
        'U': 'U',
        'V': 'V',
        'W': 'W',
        'X': 'X',
        'Y': 'Y',
        'Z': '5',
        '1': '1',
        '2': 'S',
        '3': 'E',
        '5': 'Z',
        '8': '8',
    }

    @classmethod
    def solve(cls, s):
        palindrome = True
        mirror = True
        for i in range(len(s)//2):
            if not palindrome and not mirror:
                break
            if s[i] != s[len(s) - i - 1]:
                palindrome = False
            if cls.relation.get(s[i]) != s[len(s) - i - 1]:
                mirror = False
        if len(s) % 2 == 1:
            mid = s[len(s)//2]
            if cls.relation.get(mid) != mid:
                mirror = False
        return palindrome, mirror

    @classmethod
    def print_res(cls, s):
        res = cls.solve(s)
        if res == (True, True):
            print(f"{s} -- is a mirrored palindrome.")
        elif res == (True, False):
            print(f"{s} -- is a regular palindrome.")
        elif res == (False, True):
            print(f"{s} -- is a mirrored string.")
        else:
            print(f"{s} -- is not a palindrome.")

if __name__ == '__main__':
    while True:
        try:
            s = input().strip()
            Solution.print_res(s)
        except (EOFError, KeyboardInterrupt):
            break