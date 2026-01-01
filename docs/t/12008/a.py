def solve():
    s = input()
    t = input()
    vowels = 'aeiou'
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] in vowels:
            if t[i] in vowels:
                continue
            else:
                return False
        else:
            if t[i] in vowels:
                return False
    return True


def main():
    if solve():
        print('yes')
    else:
        print('no')

if __name__ == '__main__':
    main()
