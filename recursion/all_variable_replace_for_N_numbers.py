def generate_number(N:int,M:int,prefix = None):
    """ Функция которая гененирует все числа с лидирующими
         нулями длины М в N-ричной системе счисления N<=10 """

    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N,M-1,prefix)
        prefix.pop()



def gen_bin(M,prefix=""):
    if M==0:
        print(prefix)
        return
    for digit in '0','1':
        gen_bin(M-1,prefix + digit)

gen_bin(2)
generate_number(3,3,)