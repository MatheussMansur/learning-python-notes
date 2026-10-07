# count 1 to 20 but skip multiples of 5

for i in range(1, 21):
    if i % 5 == 0:
        print("SKIP")
        continue
    print(i)

# same thing with while
count = 1
while count <= 20:
    if count % 5 != 0:
        print(count)
    count += 1
