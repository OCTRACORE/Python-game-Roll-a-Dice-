num = [x for x in range(1,11)]
f = list()
size = len(num)
for x in num:
  for i in range(2,x):
       if x % i != 0:
           f += str(x)
print(f)
