count = int()
count = int(1)
add = int()
to = int()
add = int(1)
step = int(1)
while to < 60:
    add = add/2
    count = count + add
    print(count)
    to = to + 1
    step = step + 1
    if count == 2:
        print(step)
