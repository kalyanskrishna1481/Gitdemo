

#if loop

a = 34

if a > 30:
    print("a is greater than 30", ", a value is :", a)
else:
    print("a is lesser than 30")

#for loop

summation = 0

for k in range(10, 25):
    summation =summation +1
    print(summation)
print("summation last value is :", summation)

z = 100
while z > 1:
    if z == 0:
        z = z*2
        continue
    if z == 81:
        break
    print(z)
    z = z-2
