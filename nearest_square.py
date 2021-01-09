import math
def nearest_square(num):
    if num<0:
        return 0
    num=int(math.sqrt(num))
    return num**2 