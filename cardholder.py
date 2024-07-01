class CardOlder():
    def __init__(self, cardNum, pin, firstname, lastname, balance):
        self.cardNum = cardNum
        self.pin = pin
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance
        
    # Define getters
    def get_cardNum():
        return self.cardNum
    def get_pin():
        return self.pin
    def get_firstname():
        return self.firstname  
    def get_lastname():
        return self.lastname
    def get_balance():
        return self.balance
      
    # Define setters
    def set_cardNum(self, newCard):
      self.cardNum = newCard
    def set_pin(self, newPin):
      self.pin = newPin
    def set_firstname(self, newfirst):
      self.firstname = newfirst
    def set_lastname(self, newlast):
      self.lastname = newlast
    def set_balance(self, newbalance):
      self.balance = newbalance

    def print_out(self):
      print("CardNum #": self.cardNum)
      print("pin #": self.pin)
      print("firstname #": self.firstname)
      print("lastname #": self.lastname)
      print("balance #": self.balance)



