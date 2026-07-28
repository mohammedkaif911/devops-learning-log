def miniMaxSum(arr):
    sum1 = sum(arr) - max(arr)
    sum2 = sum(arr) - min(arr)
    print(f"{sum1} {sum2}")

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)