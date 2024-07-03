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


if __name__ == "__main__":
  current_user = CardHolder("","","","")

  # create a repo for cardholder
  list_of_cardHolders = []
  list_of_cardHolders.append(CardHolder("504250324223", 973, "Rene", "Descarte", 275.24))
  list_of_cardHolders.append(CardHolder("404250324740", 832, "Malik", "Bejoux", 105.75))
  list_of_cardHolders.append(CardHolder("604250324287", 450, "Vlodmir", "Poutine", 450.89))
  list_of_cardHolders.append(CardHolder("512350378428", 654, "Dolia", "Macron", 1005.56))

# Prompt user for debit card number


try:
  debitCardNum = input("Please insert your debit card number")
  debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]

  if (len(debitMatch) > 0): 
    current_user = debitMatch[0]
    break
  else:
    print("card number not valid. Please, try again")
except:
  print("card number not valid. Please, try again")

# Prompt for the PIN
while True:
  try:
    userPin = int(input("Enter your PIN: ").strip())
    if (current_user.get_pin == userPin):
      break
    else:
      print("Invalid PIN. Please try again.")
  except:
    print("Invalid PIN. Please try again.")


# Print options
print("Welcome! ", current_user.get_firstname() " :)")
option = 0
while (option != 4):
  print_menu()
  try:
    option = int(input())
  except:
    print("Invalid input. Please try again.")

  if (option == 1):
    deposit(current_user)
  elif (option == 2):
    withdrawl(current_user)    
  elif (option == 3):
    check_balance(current_user) 
else:
  option = 0

print("Thank you. Have a nice day")
