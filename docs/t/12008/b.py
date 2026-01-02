def solve():
    n, k, m = map(int, input().split())
    l = list(map(int, input().split()))
    print(sum(l)/len(l))

def main():
    solve()

if __name__ == '__main__':
    main()
