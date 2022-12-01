# Random between 8 to 10
import random
def rand4():
    return random.random() * 4
def rand8to10():
    return rand4()/2 + 8
# Find duplicates at given x
def findDublicates(array, k):
    for i in range(len(array)):
        if i+k <len(array) and array[i] == array[i+k]:
            return i
    return -1
# Find terms for sum
def hasTerms(array, sum):
    for number in array:
        if sum - number in array[array.index(number) + 1:]:
            return True
        array.remove(number)
    return False
# Remove value from array
def remove(array, x):
    for num in range(len(array)):
        if x in array:
            array.remove(x)
    return array
# Sum of hex strings
# исправлю 
from collections import deque
def sum_hex(x, y):
    hex = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    transfer = 0
    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)
    while x:
        if y:
            res = hex[x.pop()] + hex[y.pop()] + transfer
        else:
            res = hex[x.pop()] + transfer
        transfer = 0
        if res < 16:
            result.appendleft(hex[res])
        else:
            result.appendleft(hex[res - 16])
            transfer = 1
    if transfer:
        result.appendleft('1')
    return list(result)
# a = list(input('1-е шестнадцатиричное число:').upper())
# b = list(input('2-е шестнадцатиричное число:').upper())
# print(*sum_hex(a, b))