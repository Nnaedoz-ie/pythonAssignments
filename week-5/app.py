class Footballer:
    def __init__(self, name, club, position, number):
        self.name = name
        self.club = club
        self.position = position
        self.__number = number  # Encapsulation: Making the number attribute private

    # Getter for number (encapsulation)
    def get_number(self):
        return self.__number

    # Setter for number (encapsulation)
    def set_number(self, number):
        if isinstance(number, int) and number > 0:
            self.__number = number
        else:
            raise ValueError("Number must be a positive integer")

    def introduce(self):
        return f"Hi, my name is {self.name}, I play for {self.club}, I play as a {self.position}, and I wear number {self.get_number()}."


# Subclass for Goalkeepers
class Goalkeeper(Footballer):
    def __init__(self, name, club, number, clean_sheets):
        # Inherit attributes from the parent class
        super().__init__(name, club, "Goalkeeper", number)
        self.clean_sheets = clean_sheets  # Unique attribute for goalkeepers

    # Override introduce method (Polymorphism)
    def introduce(self):
        return (
            f"Hi, I'm {self.name}, the goalkeeper for {self.club}. I wear number {self.get_number()} "
            f"and I have kept {self.clean_sheets} clean sheets this season."
        )


# Create objects
rodri = Footballer("Rodri", "Manchester City", "Defensive Midfielder", 16)
haaland = Footballer("Erling Haaland", "Manchester City", "Striker", 9)
ederson = Goalkeeper("Ederson", "Manchester City", 31, 15)

# Test the functionality
print(rodri.introduce())  # Polymorphism: Calls Footballer introduce
print(haaland.introduce())  # Polymorphism: Calls Footballer introduce
print(ederson.introduce())  # Polymorphism: Calls Goalkeeper introduce

# Encapsulation: Access and modify the private 'number' attribute safely
print(f"Ederson's number: {ederson.get_number()}")
ederson.set_number(99)
print(f"Ederson's updated number: {ederson.get_number()}")

