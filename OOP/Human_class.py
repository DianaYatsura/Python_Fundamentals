""" Create a class Human, everyone has a name, create a method in the class that displays a welcome message to each person.
Create a class method in the class that returns information that it is a species of "Homosapiens".
And in the class create a static method that returns an arbitrary message."""

class Human:
    def __init__(self, name):
        self.name = name.capitalize() if isinstance(name, str) else 'Unknown'

    def welcome_message(self):
        print(f'Hello, {self.name}!')

    @classmethod
    def species_message(cls):
        return 'Homosapiens'

    @staticmethod
    def message():
        return 'You are welcome'


h = Human('adam')
h.welcome_message()

