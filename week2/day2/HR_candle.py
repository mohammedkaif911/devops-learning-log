def birthdayCakeCandles(candles):
    maximum = max(candles)
    result = 0
    for c in candles:
        if c == maximum:
            result+=1
        else:
            pass
    return result