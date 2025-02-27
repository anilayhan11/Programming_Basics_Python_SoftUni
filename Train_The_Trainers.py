jury_count = int(input())
presentation = input()
total_grades = 0
total_sum_grades = 0.00

while presentation != 'Finish':
    average_grade = 0.00

    for i in range(jury_count):
        grade = float(input())
        average_grade += grade
        total_sum_grades += grade
        total_grades += 1

    average_grade /= jury_count
    print(f'{presentation} - {average_grade:.2f}.')

    presentation = input()

print(f'Student\'s final assessment is {total_sum_grades / total_grades:.2f}.')
