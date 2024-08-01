doing_homework: int = 12
hours_spent = 1.5
course = "Python"
assignment_time = hours_spent / float(doing_homework)
print("Курс: " + course + ", всего задач: " + str(doing_homework) + ", затрачено часов: " + str(hours_spent) +
      ", среднее время выполнения: " + str(assignment_time))