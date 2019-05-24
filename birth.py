user_age = int(input('Введите свой возраст: '))

def main(user_age):
    if user_age > 0 and user_age <= 80:
        if user_age >= 22:
            return('вот твой бейджик, топай в офис')
        elif user_age < 21 and user_age >= 17:
            return('ну ты и студентота')
        elif user_age <= 16 and user_age >= 7:
            return('ну ты и школотрон')
        elif user_age <= 6 and user_age >= 3:
            return('го в детсад')
        elif user_age <3 and user_age > 0:
            return('рожден-с, но не порабощен-с')


age_test=main(user_age)

if __name__ == "__main__":
    print(age_test)
