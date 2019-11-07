
s = 0
for num in range(100):
    if num % 2 == 1:
        s = s + num

print(num, s)

s = 0

for num in range(50):
    s = s + (2 * num + 1)
    print('2*num+1 =', 2 * num + 1)

print('final sum =', s)


for idx in range(20):
    print('*' * (idx+1))
