def staircase(n):
    hashtag = "#"
    gap = " "
    m = n - 1
    for i in range(1, n + 1):
        print(f"{gap * m}{hashtag * i}")
        m -= 1

if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)

# A HackerRank problem
