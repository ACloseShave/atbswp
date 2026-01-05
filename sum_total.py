print('Enter a whole number between 1 and 1000')

sum_total = int(input('>'))

if 1 <= sum_total <= 1000:
    for num in range(0, sum_total):
        sum_total += num
        print(sum_total)

print(f'Finished! Your final total is {sum_total}')
