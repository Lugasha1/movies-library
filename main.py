class SmartDiet:
    def __init__(self):
        self.food = {}
        self.total_calories = 0

    def register_food(self, title, calories):
        self.food[title] = calories

    def add_food(self, title, count):
        self.total_calories += self.food[title] * count

    def calculate(self):
        return self.total_calories