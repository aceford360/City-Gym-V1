#allows user to type in their height in (cm) and weight in (kg)
def calculate_bmi():
  while True:
    height = input("Please enter your height in centimetres (cm): ")
    weight = input("Please enter your weight in kilograms (kg): ")

    #program will check to see if height and weight input can be converted to float, if not, complain and allow user to try again
    try:
      height = float(height)
      weight = float(weight)
    except ValueError:
      print("Please type in numbers and try again.")
      continue

    #if number is in the negatives, complain and allow user to try again
    if height <= 0 or weight <= 0:
      print("Please try again.")
      continue
    else:
      break

#program will convert height to meters
  height = height / 100

  #calculating the bmi
  bmi = weight / (height**2)

  #completes calculating the user's bmi
  if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}.")

    #lets user know what their bmi is considered
    print("You are considered to be underweight.")
  elif bmi < 25:
    print(f"Your BMI is {bmi:.2f}")
    print("Your are considered to be normal.")
  elif bmi < 30:
    print(f"Your BMI is {bmi:.2f}.")
    print("Your are considered to be overweight.")
  else:
    print(f"Your BMI is {bmi:.2f}.")
    print("Your are considered to be obese.")


#shows weekly basic membership cost
def basic_weekly_cost():
  basic_weekly = 10
  message1 = "Weekly: $%d" % basic_weekly
  print(message1)


#calculates and prints out the monthly cost of basic membership
def basic_monthly_cost():
  basic_monthly = 10 * 52 / 12
  message2 = "Monthly: $%d" % basic_monthly
  print(message2)


#shows weekly regular membership cost
def regular_weekly_cost():
  regular_weekly = 15
  message3 = "Weekly: $%d" % regular_weekly
  print(message3)


#calculates and prints out the monthly cost of regular membership
def regular_monthly_cost():
  regular_monthly = 15 * 52 / 12
  message4 = "Monthly: $%d" % regular_monthly
  print(message4)


#shows weekly premium membership cost
def premium_weekly_cost():
  premium_weekly = 20
  message5 = "Weekly: $%d" % premium_weekly
  print(message5)


#calculates and prints out the monthly cost of premium membership
def premium_monthly_cost():
  premium_monthly = 20 * 52 / 12
  message6 = "Monthly: $%d" % premium_monthly
  print(message6)


#shows list of membership available
def display_menu():
  print("Membership Options:")
  print("1) Basic")
  print("2) Regular")
  print("3) Premium")


# allows user to choose option between three membership on menu
def display_membership_costs():
  valid = False
  while not valid:

    ask_membership = input("Please select an option: ")

    #if user chose option 1 on the display membership cost menu, show basic membership cost
    if ask_membership == "1" or ask_membership == "basic" or ask_membership == "Basic":
      print(
        "-----------------------------------------------------------------")
      print("You have chosen '1 - Basic'")
      print(
        "-----------------------------------------------------------------")
      print("Basic Rates:")
      basic_weekly_cost()
      basic_monthly_cost()
      loop_begin("Press enter to continue or any other key to exit... ")

    #if user chose option 2, go to 'display membership costs' section
    elif ask_membership == "2" or ask_membership == "regular" or ask_membership == "Regular":
      print(
        "-----------------------------------------------------------------")
      print("You have chosen '2 - Regular'")
      print(
        "-----------------------------------------------------------------")
      print("Regular Rates:")
      regular_weekly_cost()
      regular_monthly_cost()
      loop_begin("Press enter to continue or any other key to exit... ")

    #if user chose option, program will end
    elif ask_membership == "3" or ask_membership == "Premium" or ask_membership == "premium":
      print(
        "-----------------------------------------------------------------")
      print("You have chosen '3 - Premium'")
      print(
        "-----------------------------------------------------------------")
      print("Premium Rates:")
      premium_weekly_cost()
      premium_monthly_cost()
      loop_begin("Press enter to continue or any other key to exit... ")

    else:
      print("Please try again...")
      continue


#loop
def loop_begin(question):

  response = input(question)
  if response == "":

    #loops to beginning of the prorgram
    main()

  else:
    print("-----------------------------------------------------------------")
    print("You will now exit the program...")
    exit()


# allows user to choose option on the main menu
def main_menu(question):
  valid = False
  while not valid:

    response = input(question)

    #if user chose option 1 on the menu, go to BMI calculator
    if response == "1" or response == "bmi" or response == "BMI" or response == "BMI calculator" or response == "bmi calculator" or response == "BMI Calculator":
      print(
        "-----------------------------------------------------------------")
      print("You have chosen '1 - BMI Calculator'")
      print(
        "-----------------------------------------------------------------")
      calculate_bmi()
      print(
        "-----------------------------------------------------------------")
      loop_begin("Press enter to continue or any other key to exit... ")

    #if user chose option 2, go to 'display membership costs' section
    elif response == "2" or response == "display membership costs" or response == "Display membership costs" or response == "Membership costs" or response == "membership costs":
      print(
        "-----------------------------------------------------------------")
      print("You have chosen '2 - Display membership costs'")
      print(
        "-----------------------------------------------------------------")
      display_menu()
      display_membership_costs()
      print(
        "-----------------------------------------------------------------")

    #if user chose option, program will end
    elif response == "3" or response == "Exit" or response == "exit" or response == "Exit the program" or response == "exit the program":
      print("You will now exit the program...")
      exit()

    else:
      print("Please try again...")
      continue


#prints out the menu:
def main():
  print("-----------------------------------------------------------------")
  print("Version 1")  #shows the version of code
  print("-----------------------------------------------------------------")
  print("Welcome to City Gym!")
  print("-----------------------------------------------------------------")
  print("Menu:")
  print("1) BMI Calculator")
  print("2) Display membership costs")
  print("3) Exit the program")
  print("-----------------------------------------------------------------")
  main_menu("Select an option: ")


#shows main menu
main()
