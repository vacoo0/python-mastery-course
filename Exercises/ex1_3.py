sum = 0

with open('../Data/portfolio.dat', 'r') as f:
    for line in f:
        x = line.split()
        cost = int(x[1])
        amount = float(x[2])
        sum += cost * amount
    print(sum)
