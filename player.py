class Player:
    def __init__(self):
       self.name = ""
       self.symbol = ""

    def choose_name(self):
      while True:
        name = input("Enter your name: ")
        if name.isalpha():
            self.name = name
            break  
        else:
            print("Invalid name. Please enter a name with only letters.")

    def choose_symbol(self):
        while True:
            symbol = input("Choose your symbol (X or O): ").upper()
            if symbol in ["X", "O"]:
                self.symbol = symbol
                break
            else:
                print("Invalid symbol. Please choose either 'X' or 'O'.")
                
            