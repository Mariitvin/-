def sum_double_zero():
    end_sum = 0
    last_num = None
    
    while True:
        num = int(input('Введите заданные числа'))
        if num == 0:
            if last_num == 0:
                break
        else:
            end_sum += num
        
        last_num = num
    
    return end_sum

print(f"Сумма  данной последовательности: {sum_double_zero()}")



