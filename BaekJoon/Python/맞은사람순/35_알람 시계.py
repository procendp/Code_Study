h, m = map(int, input().split())

if h >= 1 and h <= 23:
    if m >=0 and m <= 44:
        print("{0} {1}".format(h - 1, m + 60 - 45))
    elif m >= 45 and m <= 59:
        print("{0} {1}".format(h, m - 45))
    
if h == 0:
    if m >=0 and m <= 44:
        print("{0} {1}".format(h + 23, m + 60 - 45))
    elif m >= 45 and m <= 59:
        print("{0} {1}".format(h, m - 45))