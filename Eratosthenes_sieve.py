A = [True for i in range(int(input())+1)]
N = len(A)
A[0] = A[1]= False
for i in range(2,N):
    if A[i]:
        for k in range(i*2,N,i):
            A[k] = False
for i in range(N):
    print(i,'-','Простое' if A[i] else 'Составное')