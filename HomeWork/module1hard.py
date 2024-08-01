students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

students_ABC = sorted(students)
student_ABC_list = tuple(students_ABC)
students_list = list(students_ABC)

students_average_rating = [(sum(grades[0]) / len(grades[0])), (sum(grades[1]) / len(grades[1])),
                           (sum(grades[2]) / len(grades[2])), (sum(grades[3]) / len(grades[3])),
                           (sum(grades[4]) / len(grades[4]))]

students_dict = {
                student_ABC_list[0]: students_average_rating[0],
                student_ABC_list[1]: students_average_rating[1],
                student_ABC_list[2]: students_average_rating[2],
                student_ABC_list[3]: students_average_rating[3],
                student_ABC_list[4]: students_average_rating[4]
                 }
print(students_dict)
