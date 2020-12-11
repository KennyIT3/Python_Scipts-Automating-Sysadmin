try:
    class Car(object): 
        def __init__(self, model, color, company, speed_limit):
            self.color = color
            self.company = company
            self.speed_limit = speed_limit
            self.model = model

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

    audi = Car("A6", "red", "audi", 160)
    print(f"\nWhat is the name of the car company: {audi.company} \nWhat is the model: {audi.model} \nWhat is the color: {audi.color} \nWhat is the car speed: {audi.speed_limit}")
    print(f"The car has now:"), audi.start()
    # audi.accelarate()
    
except(ValueError,RuntimeError):
    "The car model is incorrect"
    pass