def portfolio_cost(path):

    sum = 0
    with open(path, 'r') as f:
        for line in f:
            x = line.split()
            try:
                cost = int(x[1])
                amount = float(x[2])
                sum += cost * amount
            except ValueError as e:
                print(f'line: {line}')
                print(f'Sth wrong: {e}')


    return sum

#print(portfolio_cost('../Data/portfolio3.dat'))