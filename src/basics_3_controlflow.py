
# if statements

c = 10

if c < 5:
    print("c is smaller than 5")
elif c > 15:
    print("c is larger than 15")
else:
    print("c is between 5 and 15")

# while loops

x = 5

while x != 0:
    print(x)
    x -= 1

# we can also say
# while x, 0 will be falsy

# infinite while with break
y = 4
while True:
    y -= 4
    if y == 0:
        break

# for loops
for i in range(5):
    print(i)

# we have continue
for i in range(10):
    if i % 2:
        continue
    print(i)