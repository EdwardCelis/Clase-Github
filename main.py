for i in range(1, 31):  # Números del 1 al 30
    if i % 3 == 0 and i % 5 == 0:  # Divisible por 3 y 5
        print("FizzBuzz")
    elif i % 3 == 0:  # Divisible solo por 3
        print("Fizz")
    elif i % 5 == 0:  # Divisible solo por 5
        print("Buzz")
    else:
        print(i)  # No divisible por 3 ni por 5
