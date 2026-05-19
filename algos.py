# base = 8
# num = int(input())
# answer = ''
# while num > 0:
#     digit = num%base
#     answer += str(digit)
#     num//=base
# print(answer[::-1])

nums = [1,2,3,4,5,6]
f = False
for i in nums:
    print(f or i == 6)
