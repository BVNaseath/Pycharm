#Brandon Naseath
#B7

array = []

def sumlist(array):
    sum = 0
    for i in array:
        if sum >= 12:
            break
        else:
            sum += 1
    print(sum)



sumlist([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
sumlist([1, 1, 1])
sumlist([])
