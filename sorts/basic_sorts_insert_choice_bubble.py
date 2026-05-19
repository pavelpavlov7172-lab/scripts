from pydoc_data.topics import topics
from uuid import main


def insertion_sort(A:list):
    "Сортиврока списка А вставками"
    N = len(A)
    for top in range(1,N):
        k = top
        while k>0 and A[k-1]>A[k]:
            A[k],A[k-1] = A[k-1], A[k]
            k-=1



def choice_sort(A):
    "сортировка списка А выбором"
    N = len(A)
    for pos in range(0,N-1):
        for k in range(pos+1,N):
            if A[pos] > A[k]:
                A[k],A[pos] = A[pos],A[k]

def bubble_sort(A):
    "сортировка списка А методом пузырька"
    N = len(A)
    for bypass in range(1,N-1):
        for k in range (0, N - bypass):
            if A[k] > A[k+1]:
                A[k],A[k+1] = A[k+1],A[k]

def count_sort(A:list):
    "сортировка списка А методом подсчета"
    N = len(A)
    m = A[0]
    for i in range(1,N):
        if A[i] > m:
            m = A[i]
    D = [0] * (m+1)
    for i in A:
        D[i] +=1
    k = 0
    for number in range(len(D)):
        for i in range(D[number]):
            A[k] = number
            k +=1


def test_sort(sort_algorithm):
    print("тестируем", sort_algorithm.__doc__)
    print("testcase 1: ", end = "")
    A = [1,2,6,4,3,2,9]
    A_sorted = [1,2,2,3,4,6,9]
    sort_algorithm(A)
    print('OK' if A==A_sorted else "Fail")

    print("testcase 2: ", end="")
    A = [1, 2, 5, 4, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print('OK' if A == A_sorted else "Fail")

    print("testcase 3: ", end="")
    A = [1, 2, 6, 4, 3, 2]
    A_sorted = [1, 2, 2, 3, 4, 6]
    sort_algorithm(A)
    print('OK' if A == A_sorted else "Fail")

if __name__ == "__main__" :
    test_sort(insertion_sort)
    test_sort(choice_sort)
    test_sort(bubble_sort)
    test_sort(count_sort)