from carHolder import cardHolder

def print_menu():
  # Print the options to the user
  print("Welcome! choose one option from the following ")
  print("1. Deposit")
  print("2. Withdrawl")
  print("3. Show alance")
  print("4. Exit")


def deposit(cardHolder):
  try:
    deposit_amount = float(input("How much do you want to deposit? $"))
    cardHolder.set_balance(cardHolder.get_balance() + deposit_amount)
    print(f"You have sucessfully deposit {deposit_amount}. Your new balance is {str(cardHolder.get_balance())}")
  except:
    print("Invalid Input")


def withdrawl(cardHolder):
  try:
    withdrawl_amount = float(input{"How much would you like to withdrawl? $")
    if cardHolder.get_balance() < withdrawl_amount:
      print("Operation not valid: insufficient amount! :(")
    else:
      cardHolder.set_balance(cardHolder.get_balance() - withdrawl_amount)
      print(f"You have sucessfully withdrawl {withdrawl_amount}. Your new balance is {str(cardHolder.get_balance()}")
  except:
  print("Invalid Input")

def check_balance(cardHolder):
  print("Your balance is: ", cardHolder.get_balance())

    
