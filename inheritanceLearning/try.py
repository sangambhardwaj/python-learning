# prime number

# n1 = int(input("starting point"))
# n2 = int(input("last point"))
#
# empt_list = []
# for numb in range(n1, n2+1):
#     for i in range(2, numb // 2):
#         if numb % i == 0:
#             break
#     else:
#         empt_list.append(numb)
# print(empt_list)
#


n = 24

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")
