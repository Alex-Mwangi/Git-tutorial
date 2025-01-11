

number_of_students = int(input("Enter the number of sudents: "))

name_score = []

for stud in range(1, number_of_students+1):
    name = input(f"Ener the name of student {stud}: ")
    score = int(input(f"Enter the score of student {stud}: "))

    name_score.append((name, score))

name_score.sort(key=lambda x: x[1], reverse=True)


# print(f'{name_score[0][0]} score {name_score[0][1]}')
# print(f'{name_score[1][0]} score {name_score[1][1]}')

print(name_score)