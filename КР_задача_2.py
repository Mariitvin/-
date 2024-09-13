def sum_row(n):
    end_sum = sum(1 / (i**2) for i in range(1, n + 1))
    return end_sum

n = int(input())
print( f"Сумма ряда: {sum_row(n)}" )


