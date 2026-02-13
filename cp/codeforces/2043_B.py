total_cases = int(input())

for case in range(total_cases):

    n, d = input().split()
    n = int(n)
    d_int = int(d)
    answers = [1]
    sum_of_digits = n * d_int
    if sum_of_digits % 3 == 0:
        answers.append(3)
    if sum_of_digits % 9 == 0:
        answers.append(9)

    if d_int % 5 == 0:
        answers.append(5)

    # last_digit = d_int
    # double_last_digit = 2 * last_digit
    # subtraction_res =

    full_number = int(str(d_int) * n)
    # print(full_number % 7)

    if (full_number % 7) == 0:
        answers.append(7)

    print(" ".join(map(str, sorted(answers))))
