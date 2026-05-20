def matryoshka(n):
    if n==1:
        print("Самая маленькая матрешка")
    else:
        print("Матёркша n =",n)
        matryoshka(n-1)
        print("Низ матрёшки n =",n)

if __name__ == "__main__":
    matryoshka(5)