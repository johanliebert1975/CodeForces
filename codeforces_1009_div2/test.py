from c import calc_y

for i in range(1, 100):
    x = calc_y(i)
    if x != -1:
        print(i,x)

