days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

arrivalDay = 0
maxDuration = 0
parkingDuration = 0
validDuration = False

# **CAR PARK PAYMENT SYSTEM SIMULATOR**
# This simulates the car park system and currently does
# not have any "automated" functions such as barcode or ticket reading.
# All data will be entered manually for testing.
runParking = True

#  MAIN LOOP
while runParking:
    print("Welcome to the Car Park Payment System")

    print('''Please input the following information:
        Day of arrival
        Hour of arrival
        Duration of stay 
        and frequent parking number (if you have one)

        Please press ENTER to continue or QUIT to exit the program
    ''')
    cpStart = input().upper()
    if cpStart == "":
        validDay = False
        # Get Arrival Day
        while not validDay:
            print("""Enter day: 
            1: Sunday
            2: Monday
            3: Tuesday
            4: Wednesday
            5: Thursday
            6: Friday
            7: Saturday
            """)
            # What is the purpose of this try/Except block?
            # Wht does the try/except do?
            try:
                arrivalDay = int(input(">> "))
            except:
                print("Not an integer")
            else:
                if arrivalDay <1:
                    print("<0")
                elif arrivalDay >7:
                    print(">7")
                else:
                    validDay = True
            
        print(f"Arrival day: {days[arrivalDay-1]}")
        
        # Q: What is the purpose of this selection block?
        if arrivalDay == 1:
            maxDuration = 8
        elif arrivalDay == 7:
            maxDuration = 4
        else:
            maxDuration = 2


        # -- Your comments: What is this next block for?
        validDuration = False
        while validDuration == False:
            try:
                print("Enter the duration of your stay, up to a maximum of", maxDuration, "hours")
                parkingDuration = int(input(">> "))
            except:
                print("Must be a number")
            else:
                # What type of validation is in use here?
                if parkingDuration < 1:
                    print ("must be 1 or more")
                elif parkingDuration > maxDuration:
                    print("Must be ", maxDuration, "or less")
                else: 
                    validDuration = True
    elif cpStart == "QUIT":
        runParking = False

    # CONTINUE YOUR CODE HERE

    # Complete requirements for task 1:
    # Ask if there is a Frequent Parking Number
    #  IF YES - enter the 5 digit code
    # Check if the code is valid
    #       the 5th digit is the check digit. 
    #  If VALID - apply discount
    # Calculate the cost
    # Deduct discount is applicable
    # Output the final cost
    #       
    # How can you check that it is the correct checkdigit?
    # Have you used the correct prices?
    # Is the price correct for the time of day?


