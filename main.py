class Human:
    """
    Это реально оописание класса?
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Human {self.name}"


popular_names = ["Дамир", "Данил", "Айнур", "Андрей", "Витя", "Булат", "Марсель"]
humanity = []

hum = Human("Admin")
for name in popular_names:
    hum = Human(name)
    humanity.append(hum)

for hum in humanity:
    print(hum, end=" ")
print()
print(humanity)