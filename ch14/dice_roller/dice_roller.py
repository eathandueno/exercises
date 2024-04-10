from dice import Dice, Die

def main():
    print("The Dice Roller program")
    
    # Create a Dice object
    dice = Dice()

    # Display the 6 die images using a loop
    for i in range(1, 7):
        die = Die(i)
        print(die.image)

    # Add a method named getTotal() in the Dice class
    class Dice:
        def __init__(self):
            self.dice = [Die() for _ in range(2)]

        def roll_all(self):
            for die in self.dice:
                die.roll()

        def getTotal(self):
            return sum(die.value for die in self.dice)

    # Display the total each time the user rolls the dice
    dice.roll_all()
    print("Total value of dice: ", dice.getTotal())
if __name__ == "__main__":
    main()
