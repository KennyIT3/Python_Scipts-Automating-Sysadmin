#function
#Python

def basketball(Height, Weight, Age):
    # print("Attrubutes of different players")
    attrubutes = ['Height=' " 5ft" , 'Weight=' ' 170Pounds', 'Age=' ' 20']
    for cool in attrubutes:
        # print(" Here is my height", {cool.height()} )
        print(f"Here are the attrubutes:", cool)
        # person = {'first': first_name, 'last': last_name} #Dictionary
# test = basketball({'5'}, {'170'}, {'26'})
# height = basketball("5'2")
# weight = basketball("170 pounds")
# age= basketball('26')
basketball('Height', 'Weight', 'Age')


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
