#
# a = " hello world "
# print(a.rjust(19,'#'))
#
# print(a.ljust(16,"#"))
# print(a.center(22,"&"))
# print(a.zfill(55))


d = '{:0=6d}'.format(-125)
print(type(d))
print(d)








# write python code to print all prime numbers between 100 to 200

def num_prime():
    for numb in range(100,201):
        for i in range(2,numb//2):
            if numb%i==0:
                break
        else:
            print(numb,end=' ')

num_prime()




