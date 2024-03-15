def calculate_score(quiz_result):
    score = 0
    combo = 0

    for answer in quiz_result:
        if answer == 'O':
            combo += 1
            score += combo
        else:
            combo = 0

    return score


test_cases = int(input())

for _ in range(test_cases):
    quiz_result = input()
    print(calculate_score(quiz_result))
