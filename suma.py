from typing import List

def suma(nums: List[int]) -> int:
    cont= 0
    for n in nums:
        cont+= n
    return cont

def is_integer(target):
    try:
        int(target)
        return True
    except:
        return False

