def wordle_checker(guess, target):
    array_result = [0, 0, 0, 0, 0]

    for num in range(5):
        if guess[num] == target[num]:
            array_result[num] = 2

    array_of_strings = map(str, array_result)
    return "".join(array_of_strings)
