

def change(amount, pennies, nickles, dimes, quarters):
    amount *= 1.06
    cents = amount - int(amount)
    cents = round(cents, 2)
    # pennyAmount = pennies * .01
    # nicklesAmount = nickles * .05
    # dimesAmount = dimes * .1
    # quartersAmount = quarters * .25
    gemini = True
    quarter = 0
    dime = 0
    nickle = 0
    penny = 0

    while not cents == 0: #and not (quarters == 0 and dimes == 0 and nickles == 0 and pennies == 0):

        while not quarters <= 0 and gemini:
            # if cents % .25 <= 24: #and cents <= quartersAmount:
            cents -= .25
            quarters -= 1
            if not int(cents % 25) == 0:
                gemini = False
                cents += 0.25
                quarters += 1
                quarter -= 1
            quarter += 1
        gemini = True
        while not dimes <= 0 and cents > 0 and gemini:
            #if int((cents - quartersAmount)) % 0.10 <= 9: #and cents <= (quartersAmount + dimesAmount):
                # cents = cents - (0.25 * quarters)
                # quarters = 0
                #quartersAmount = 0
                cents -= 0.1
                dimes -= 1
                if not int(cents % 10) == 0:
                    gemini = False
                    cents += 0.10
                    dimes += 1
                    dime -= 1
                if cents.__abs__() < 0.001:
                    cents = 0
                dime += 1
        gemini = True
        while not nickles <= 0 and cents > 0 and gemini:
            #if int((cents - (quartersAmount + dimesAmount))) % 0.05 <= 4: #and cents <= (quartersAmount + dimesAmount + nicklesAmount):
                # cents = cents - (0.25 * quarters)
                # quarters = 0
                # quartersAmount = 0
                # cents = cents - (0.10 * dimes)
                # dimes = 0
                # dimesAmount = 0
                cents -= 0.05
                nickles -= 1
                if not int((cents) % 5) == 0:
                    gemini = False
                    cents += 0.05
                    nickles += 1
                    nickle -= 1
                if cents.__abs__() < 0.001:
                    cents = 0
                nickle += 1

        while not pennies <= 0 and cents > 0: #and int(cents % 1) == 0:
            #if int((cents - (quartersAmount + dimesAmount + pennyAmount))) % 0.01 == 0: #and cents <= (quartersAmount + dimesAmount + nicklesAmount + pennyAmount):
                # cents = cents - (0.25 * quarters)
                # quarters = 0
                # quartersAmount = 0
                # cents = cents - (0.10 * dimes)
                # dimes = 0
                # dimesAmount = 0
                # cents = cents - (0.05 * nickles)
                # #nickles = 0
                # nicklesAmount = 0
                cents -= 0.01
                pennies -= 1
                if cents.__abs__() < 0.001:
                    cents = 0
                penny += 1
        # print(cents)
        # print(int(cents % 5))
        if not cents == 0:
            print("You don't have the perfect change")
            break
        else:
            print("Total due: " + '${:,.2f}'.format(amount))
            print("Perfect change for: " + '${:,.2f}'.format(amount - int(amount)))
            break
    print("You need", quarter, "quarters")
    print("You need", dime, "dimes")
    print("You need", nickle, "nickles")
    print("You need", penny, "pennies")
    print("Remaining due:", cents)

        # if cents % 0.1 == 0 and cents < dimesAmount:
        #     cents -= 0.1
        #     dimes -= 1
        # if cents % 0.05 == 0 and cents < nicklesAmount:
        #     cents -= 0.05
        #     nickles -= 1
        # if cents % 0.01 == 0 and cents < pennyAmount:
        #     cents -= 0.01
        #     pennies -= 1


def changePennyPriority(amount, pennies, nickles, dimes, quarters):
    # amount *= 1.06
    cents = amount - int(amount)
    cents = round(cents, 2)
    cents1 = cents
    gemini = True
    quarter = 0
    dime = 0
    nickle = 0
    penny = 0

    while not cents == 0:

        while not pennies <= 0 and cents > 0:
                cents = round(cents, 2)
                if ((cents * 100) % 10 == 0 or (cents * 100) % 5 == 0) and ((quarters * 0.25 + dimes * 0.10 + nickles * 0.05) >= cents):
                    break
                cents -= 0.01
                pennies -= 1
                if cents.__abs__() < 0.001:
                    cents = 0
                penny += 1
        # print((cents * 100) % 5)
        while not nickles <= 0 and cents > 0:
                cents = round(cents, 2)
                if (cents * 100) % 10 == 0 and ((quarters * 0.25 + dimes * 0.10) >= cents):
                    break
                cents -= 0.05
                nickles -= 1
                # if not int((cents) % 5) == 0:
                #     gemini = False
                #     cents += 0.05
                #     nickles += 1
                #     nickle -= 1
                if cents.__abs__() < 0.001:
                    cents = 0
                nickle += 1

        while not dimes <= 0 and cents > 0:
            cents = round(cents, 2)
            if (cents * 100) % 25 == 0 and ((quarters * 0.25) >= cents):
                break
            cents -= 0.1
            dimes -= 1
            # if not int(cents % 10) == 0:
            #     gemini = False
            #     cents += 0.10
            #     dimes += 1
            #     dime -= 1
            if cents.__abs__() < 0.001:
                cents = 0
            dime += 1

        while not quarters <= 0 and cents > 0:
            cents = round(cents, 2)
            if (cents - .25) < 0:
                break
            cents -= .25
            quarters -= 1
            # if not int(cents % 25) == 0:
            #     gemini = False
            #     # cents += 0.25
            #     # quarters += 1
            #     # quarter -= 1
            if cents.__abs__() < 0.001:
                cents = 0
            quarter += 1
        #print(cents)

        if not cents == 0:
            print("You don't have the perfect change")
            change = True
            while not cents < 0 and change:

                if quarters == 0 and dimes == 0 and nickles == 0 and pennies == 0:
                    change = False

                while not pennies <= 0 and cents > 0:
                    cents -= 0.01
                    pennies -= 1
                    penny += 1

                while not nickles <= 0 and cents > 0:
                    cents -= 0.05
                    nickles -= 1
                    nickle += 1

                while not dimes <= 0 and cents > 0:
                    cents -= 0.1
                    dimes -= 1
                    dime += 1

                while not quarters <= 0 and cents > 0:
                    cents -= .25
                    quarters -= 1
                    quarter += 1
            print("Alternatively you could pay", penny, "pennies")
            print(nickle, "nickles")
            print(dime, "dimes")
            print(quarter, "quarters")
            print("With the minimum coin change of" + '${:,.2f}'.format((quarter * 0.25 + dime * 0.10 + nickle * 0.05 + penny * 0.01) - cents1))
            break
        else:
            print("Total due: " + '${:,.2f}'.format(amount))
            print("Perfect change for: " + '${:,.2f}'.format(amount - int(amount)))
            print("You need", quarter, "quarters")
            print("You need", dime, "dimes")
            print("You need", nickle, "nickles")
            print("You need", penny, "pennies")
            print("Remaining due:", cents)
            break


catch = True
while catch:
    try:
        amount = float(input("Enter the amount you need to pay: "))
        penny = int(input("Number of pennies"))
        nickle = int(input("Number of nickles"))
        dime = int(input("Number of dimes"))
        quarter = int(input("Number of quarters"))
        catch = False
    except ValueError:
        print("You need to enter proper values.")


changePennyPriority(amount, penny, nickle, dime, quarter)



