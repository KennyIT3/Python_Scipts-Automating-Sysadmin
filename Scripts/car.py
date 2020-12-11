try:
    class Car(object): 
        def __init__(self, year, model, color, company, speed_limit):
            self.color = color
            self.company = company
            self.speed_limit = speed_limit
            self.model = model
            self.year = year

        def start(self):
            print("started")

        def stop(self):
            print("stopped")

        def accelarate(self):
            print("accelarating...")
            "accelarator functionality here"

        def change_gear(self, gear_type):
            print("gear changed")
            " gear related functionality here"
            
        if __name__ == "__main__":
            print("\nHere is the car details:")
            # print("\n")

    jaguar = Car("2020", "F-Type", "Black", "Jaguar", 260)
    print(f" \nWhat is the car year: {jaguar.year}\nWhat is the name of the car company: {jaguar.company} \nWhat is the model: {jaguar.model} \nWhat is the color: {jaguar.color} \nWhat is the car speed: {jaguar.speed_limit}")
    print(f"The car has now:"), jaguar.start()
    # audi.accelarate()

except(ValueError,RuntimeError):
    "The car details is incorrect"
    pass