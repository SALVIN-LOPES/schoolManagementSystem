import json
import math

def frequency1(Dividend,Divisor,Number_of_Digits):
    ans = Dividend/Divisor
    frac, whole = math.modf(ans)
    val = str(frac)
    d = {}
    for i in range(2,Number_of_Digits+2):
        if val[i] in d:
            d[str(val[i])] += 1
        else:
            d[str(val[i])] = 1
    print(json.dumps(d, sort_keys=True))

frequency1(22,7,10)