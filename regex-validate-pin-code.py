# Nicole Carman
# Codewars kata - Regex validate PIN code
# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits. If the function is passed a valid PIN string, return true, else return false.

# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false


def validate_pin(pin):
    
    if pin.isdigit() and (len(pin) == 4 or len(pin) == 6):
      response = True
        
      for i in range(len(pin)):
        if (pin[i] not in "1234567890"):
          response = False
        else:
          response = True
                
      if (response):
          return True
      else:
          return False
    else:
          return False