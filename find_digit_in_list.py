def array_search(L:list,N:int, x:int):
    "Поиск значения x  в массиве L размером N"
    for k in range(N-1):
        if L[k] == x:
            return k
    return -1

def test_array_serch():
    A = [1,2,3,4,5]
    m = array_search(A,5,8)
    if m == 4:
        print("Test 1 - ok")
    else:
        print("Test 1 - False")

    A2 = [-1, -2, -3, -34, -5]
    m = array_search(A2, 5, -2)
    if m == 1:
        print("Test 2 - ok")
    else:
        print("Test 2 - False")

    A3 = [10, 2, 30, 10, 10]
    m = array_search(A, 5, 10)
    if m == 0:
        print("Test 3 - ok")
    else:
        print("Test 3 - False")

test_array_serch()