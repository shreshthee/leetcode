print("Input a number, input exit to exit.")



class solution:
  #We define a function to check if a string has a number.

  #Using floats for this is unecessary since the concept is only really needed with integers but we will anyway.
  def is_number(s):
    try:
        float(s) #If we can convert the string to a float it is a number and thus we return True
        return True
    except ValueError:
        return False
  def __init__(inp)
    if is_number(inp): #We check if the input is a number.
      num = float(inp) #We convert the string to a float.
      if (num % 2) == 0: # We check if the number is even.
        print("{0} is Even".format(num))
      else:
        print("{0} is Odd".format(num))
    else: #The string is not a number.
        print("Input is not a number.")
