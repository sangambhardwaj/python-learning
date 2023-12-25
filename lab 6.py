family = ['suneel', 'shekhar', ('sanjay', 'vijay'), 'vivek', 'vikas', 'shivam', 'sangam', 'sagar', 'satyam', 'piyush',
          2, 6, 8, 1, True, 1]
#       [0,             1,              2,          3,      4,      5,      6,        7,        8,      9]
print(type(family))
print(family[-4])
print(family[2][1])
print(family.append(123))
print(family.insert(6, 567))
print(family.remove('shivam'))
a = family[-1]
print(a)
family.remove(a)

# = assinment operater
print(type(family))
print(family)
family1 = 'suneel',  # 'shekhar'#,'sanjay','vijay','vivek','vikas','shivam','sangam','sagar','satyam','piyush'
print(type(family1))
print(family1)
