def age():
    try:
        age = int(input('Age: '))
        year = int(input('Year: '))
        salary = int(100000)
        risk = salary / age / year
        print(risk)
    except ZeroDivisionError:
        print("Can't divide by this number")
    except ValueError:
        print("Not a numerical value")
age()

