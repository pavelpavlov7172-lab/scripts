def array_inversion(A:list,N:int):
    "Поиск значения x  в массиве L размером N"
    B = [0] * N
    print(A)
    for k in range(len(A)):
        B[k] = A[len(A)-1-k]
    # for k in range(N//2):
    #     A[k],A[N-k-1] = A[N-k-1],A[k]
    print(B)
    return B

def test_array_serch():
    A = [1,2,3,4,5]
    m = array_inversion(A,5)
    if m == [5,4,3,2,1]:
        print("Test 1 - ok")
    else:
        print("Test 1 - False")




test_array_serch()