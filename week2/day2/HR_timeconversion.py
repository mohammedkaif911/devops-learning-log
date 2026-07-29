def timeConversion(s):
    hours = s[:2]
    stamp = s[-2:]
    if stamp == "AM":
        if hours=="12":
            hours="00"
        else:
            pass
        
    # Write your code here
    else:
        if hours!="12":
            hours = int(hours)+12
        else:
            pass
        
    return f"{hours}{s[2:-2]}"