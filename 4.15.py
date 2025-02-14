yb = int(input("Укажите год рождения: "))
mb = int(input("Укажите месяц рождения: "))
ytd = int(input("Укажите сегодняшний год: "))
mtd = int(input("Укажите сегодняшний месяц: "))

age = (ytd*12+mtd-(yb*12+mb))//12

print(age)
