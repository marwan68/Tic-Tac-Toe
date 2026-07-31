class Menu:
  def display_main_menu(self):
    print("Welcome to the Main Menu")
    print("1. Start Game")
    print("2. Exit")  
    while True:
      choice = input("Enter your choice (1 or 2): ")
      if choice in ("1", "2"):
       return choice
      print("Invalid choice. Please enter 1 or 2.")
  

  def display_end_game_menu(self):
    print("Game over")
    print("1. Play Again")
    print("2. Quit Game")  
    while True:
      choice = input("Enter your choice (1 or 2): ")
      if choice in ("1", "2"):
        return choice
      print("Invalid choice. Please enter 1 or 2.")