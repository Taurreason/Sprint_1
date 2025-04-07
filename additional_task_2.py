def digit_root(num):

    if num > 10**7:
        raise ValueError('Число не должно превышать 10 в 7 степени')

    while num >= 10:  # Повторяем, пока число не станет однозначным
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
        num = sum  # Заменяем число на сумму его цифр
    return num


print(digit_root(889987))