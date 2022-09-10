def tax_calculator(income):
    return income * 0.35

def pay_tax(tax):
    print("Thank you for paying", tax)

def say_hello(name="anonymous"):
    print("hello", name)

def plus(a=0, b=0):
    print(a + b)

def minus(a=0, b=0):
    print(a - b)

def mul(a=1, b=1):
    print(a * b)

def div(a=1, b=1):
    print(a / b)

def power(a=0, b=0):
    print(a ** b)

my_name = "nico"
my_age = 12
my_color_eyes = "brown"

print(f"Hello I'm {my_name}, I have {my_age} years in the earth, {my_color_eyes} is my eye color")

def make_juice(fruit):
    return f"{fruit}+🥤"

def add_ice(juice):
    return f"{juice}+🧊"

def add_sugar(iced_juice):
    return f"{iced_juice}+🍷"

juice = make_juice("🍉")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)