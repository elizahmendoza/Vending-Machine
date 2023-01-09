def vend():
    # list of available items within the vending machine
    a = {'code': '10','item': 'Choco Mallows', 'price': 2.75, 'stock': 4}
    b = {'code': '11','item': 'Oreo Cookies', 'price': 2.50, 'stock': 5}
    c = {'code': '12','item': 'Pocky Biscuit Sticks', 'price': 1.75, 'stock': 3}
    d = {'code': '13','item': 'Hello Panda Biscuits', 'price': 1.50, 'stock': 8}
    e = {'code': '14','item': 'Cheese Croissant', 'price': 2.00, 'stock': 7}
    f = {'code': '15','item': 'Fanta Soft Drink', 'price': 3.00, 'stock': 5}
    g = {'code': '16','item': 'Frappuccino Iced Coffee', 'price': 3.50, 'stock': 7}
    h = {'code': '17','item': 'Sparkling Water', 'price': 2.25, 'stock': 4}
    i = {'code': '18','item': 'Cranberry Juice', 'price': 2.50, 'stock': 6}
    j = {'code': '19','item': 'Strawberry Drink', 'price': 2.25, 'stock': 5}
    S_variation = ['SNACKS','SNACKS ',' SNACKS','Snacks','Snacks ',' Snacks','snacks','snacks ',' snacks'] # variations of "snacks" for better user experience
    D_variation = ['DRINKS','DRINKS ',' DRINKS','Drinks','Drinks ',' Drinks','drinks','drinks ',' drinks'] # variations of "drinks" for better user experience
    A_variation = ['ALL','ALL ',' ALL','All','All ',' All','all','all ',' all'] # variations of "all" for better user experience
    Snacks = [a, b, c, d, e] # snacks category
    N_Snacks = ['Choco Mallows','Oreo Cookies','Pocky Biscuit Sticks','Hello Panda Biscuits','Cheese Croissant'] # list used for suggesting a "snack"
    Drinks = [f, g, h, i, j] # drinks category
    N_Drinks = ['Fanta Soft Drink','Frappuccino Iced Coffee','Sparkling Water','Cranberry Juice','Strawberry Drink'] # list used for suggesting a "drink"
    Items = [a, b, c, d, e, f, g, h, i, j] # all items
    cim = 0 # cash in machine
    Yes = ['YES','YES ',' Yes','Yes','Yes ',' Yes','Y','Y ',' Y','yes','yes ',' yes','y','y ',' y'] # variations of "yes" for better user experience
    No = ['NO','NO ',' NO','No','No ',' No','N','N ',' N','no','no ',' no','n','n ',' n'] # variations of "no" for better user experience
    Power_Supply = True # main vending machine loop code
    import random # used for suggesting items
   
    while Power_Supply == True: # if "Power_supply" is true = code will continue to loop starting from "Welcome to vending machine!"
        print('\nWelcome to vending machine!')
        L_Category = True # activates "L_Category" loops
        query = input('Do you wish to proceed (Yes/No): ')
        if query in Yes: # if "Variable" is within the variations of "Yes" = user will be able to use the vending machine
            while L_Category == True: # if "L_Category" is true = code will continue to loop starting from "Do you wish to proceed?"
                Category = input('\nWhat do you wish to buy (Snacks/Drinks/All): ')
                S_Quit = False # if "Quit" is false = corresponding category loop will continues
                D_Quit = False
                A_Quit = False
                if Category in S_variation: # if "Variable Value" is within the "Variation" list = user will be able to access the snacks only area of the vending machine
                    def show(Snacks):
                        print('\nItems Available: \n*****************')
               
                        for Snack in Snacks:      
                            if Snack.get('stock') == 0: # if a certain "Item" within the "List" has "0 Stocks" = "Item" gets "Removed"
                                Snacks.remove(Snack)
                        for Snack in Snacks:
                            print(f"\nCode: {Snack['code']} | Item: {Snack['item']} | Price: {Snack['price']} | Stock: {Snack['stock']}") # this code lists the menu of "Snacks"
               
                        print('*********************************************************\n')  
               
                   
                    while S_Quit == False: # if "Quit" is false = corresponding category loop continues
                        show(Snacks)
                        selected = input('Enter the exact code of the item you want to purchase: ') # code to choose a specific "Item" in the vending machine
                        for Snack in Snacks:
                            if selected == Snack.get('code'): # chosen "Item" will provide code & price
                                selected = Snack              
                                price = selected.get('price')
                                while cim < price: # if "cim" is less than "price" = loop will continue
                                    cim = float(input('Please insert $' + str(price - cim) + ': '))
                                else:
                                    print('\nYou have received ' + selected.get('item') + '.') # shows user can "receive" the item
                                    selected['stock'] -= 1 # chosen "item" gets "-1 stock" everytime code activates until vending machine is "Rebooted/Restarted"
                                    cim -= price # "cim" minus the "price" of chosen item = overwritten value of "cim"
                                    print('Cash remaining: $'+str(cim) + '.')
                                    print('\nSuggested drink for the item you bought is the "' + random.choice(N_Drinks) + '".') # code "random.choice" takes 1 item from "list" and shows
                                    a = input('Would you like to add another item? (Yes/No): ') # redirects user depending on users "choice"
                                    if a in No:
                                        print('\n______________________________________________________\n')
                                        import datetime # current date and time
                                        x = datetime.datetime.now() # inputting current date and time within the variable "x"
                                        print(x) # provides "date" & "time"
                                        print('A total amount of $' + str(cim) + ' has been refunded.')
                                        cim = 0
                                        print('Thank you for using the vending machine, have a nice day!')
                                        print('\n______________________________________________________\n')
                                        S_Quit = True # "cancels" corresponding loop
                                        L_Category = False # "cancels" corresponding loop
                                        break
                                    elif a in Yes:
                                        S_Quit = True # "cancels" corresponding loop
                                        break
                                    else:
                                        print('\nYour answer "{}" is invalid.'.format(a))
                                        print('\n______________________________________________________\n')
                                        import datetime # current date and time
                                        x = datetime.datetime.now() # inputting current date and time within the variable "x"
                                        print(x) # provides "date" & "time"
                                        print('A total amount of $' + str(cim) + ' has been refunded.')
                                        cim = 0
                                        print('Thank you for using the vending machine, have a nice day!')
                                        print('\n______________________________________________________\n')
                                        S_Quit = True # "cancels" corresponding loop
                                        L_Category = False # "cancels" corresponding loop
                                        break
                        else:
                            print('ERROR: Sorry, that item is not available. Please select another item.')
                            continue
                elif Category in D_variation: # if "Variable Value" is within the "Variation" list = user will be able to access the drinks only area of the vending machine
                    def show(Drinks):
                        print('\nItems Available: \n*****************')
               
                        for Drink in Drinks:      
                            if Drink.get('stock') == 0: # if a certain "Item" within the "List" has "0 Stocks" = "Item" gets "Removed"
                                Drinks.remove(Drink)
                        for Drink in Drinks:
                            print(f"\nCode: {Drink['code']} | Item: {Drink['item']} | Price: {Drink['price']} | Stock: {Drink['stock']}") # this code lists the menu of "Drinks"
               
                        print('**********************************************************\n')  
               
 
                    while D_Quit == False: # if "Quit" is false = corresponding category loop continues
                        show(Drinks)
                        selected = input('Enter the exact code of the item you want to purchase: ') # code to choose a specific "Item" in the vending machine
                        print()
                        for Drink in Drinks:
                            if selected == Drink.get('code'): # chosen "Item" will provide code & price
                                selected = Drink              
                                price = selected.get('price')
                                while cim < price: # if "cim" is less than "price" = loop will continue
                                    cim = float(input('Please insert $' + str(price - cim) + ': '))
                                else:
                                    print('\nYou have received ' + selected.get('item')) # shows user can "receive" the item
                                    selected['stock'] -= 1 # chosen "item" gets "-1 stock" everytime code activates until vending machine is "Rebooted/Restarted"
                                    cim -= price # "cim" minus the "price" of chosen item = overwritten value of "cim"
                                    print('Cash remaining: $' + str(cim))
                                    print('\nSuggested drink for the item you bought is the "' + random.choice(N_Snacks) + '".') # code "random.choice" takes 1 item from "list" and shows
                                    a = input('Would you like to add another item? (Yes/No): ') # redirects user depending on users "choice"
                                    if a in No:
                                        print('\n______________________________________________________\n')
                                        import datetime # current date and time
                                        x = datetime.datetime.now() # inputting current date and time within the variable "x"
                                        print(x) # provides "date" & "time"
                                        print('A total amount of $' + str(cim) + ' has been refunded.')
                                        cim = 0
                                        print('Thank you for using the vending machine, have a nice day!')
                                        print('\n______________________________________________________\n')
                                        D_Quit = True # "cancels" corresponding loop
                                        L_Category = False # "cancels" corresponding loop
                                        break
                                    elif a in Yes:
                                        D_Quit = True # "cancels" corresponding loop
                                        break
                                    else:
                                        print('\nYour answer "{}" is invalid.'.format(a))
                                        print('\n______________________________________________________\n')
                                        import datetime # current date and time
                                        x = datetime.datetime.now() # inputting current date and time within the variable "x"
                                        print(x) # provides "date" & "time"
                                        print('A total amount of $' + str(cim) + ' has been refunded.')
                                        cim = 0
                                        print('Thank you for using the vending machine, have a nice day!')
                                        print('\n______________________________________________________\n')
                                        D_Quit = True # "cancels" corresponding loop
                                        L_Category = False # "cancels" corresponding loop
                                        break
                        else:
                            print('ERROR: Sorry, that item is not available. Please select another item.')
                            continue
                elif Category in A_variation: # if "Variable Value" is within the "Variation" list = user will be able to access all the items within the vending machine
                    def show(Items):
                        print('\nItems Available: \n*****************')
               
                        for Item in Items:      
                            if Item.get('stock') == 0: # if a certain "Item" within the "List" has "0 Stocks" = "Item" gets "Removed"
                                Items.remove(Item)
                        for Item in Items:
                            print(f"\nCode: {Item['code']} | Item: {Item['item']} | Price: {Item['price']} | Stock: {Item['stock']}") # this code lists the menu of "Snacks" and "Drinks"
               
                        print('**********************************************************\n')  
               
                   
                    while A_Quit == False: # if "Quit" is false = corresponding category loop continues
                        show(Items)
                        selected = input('Enter the exact code of the item you want to purchase: ') # code to choose a specific "Item" in the vending machine
                        print()
                        for Item in Items:
                            if selected == Item.get('code'): # chosen "Item" will provide code & price
                                selected = Item              
                                price = selected.get('price')
                                while cim < price: # if "cim" is less than "price" = loop will continue
                                    cim = float(input('Please insert $' + str(price - cim) + ': '))
                                else:
                                    if selected in Snacks:
                                        print('\nYou have received ' + selected.get('item')) # shows user can "receive" the item
                                        selected['stock'] -= 1 # chosen "item" gets "-1 stock" everytime code activates until vending machine is "Rebooted/Restarted"
                                        cim -= price # "cim" minus the "price" of chosen item = overwritten value of "cim"
                                        print('Cash remaining: $' + str(cim))
                                        print('\nSuggested drink for the item you bought is the "' + random.choice(N_Drinks) + '".') # code "random.choice" takes 1 item from "list" and shows
                                        a = input('Would you like to add another item? (Yes/No): ') # redirects user depending on users "choice"
                                        if a in No:
                                            print('\n______________________________________________________\n')
                                            import datetime # current date and time
                                            x = datetime.datetime.now() # inputting current date and time within the variable "x"
                                            print(x) # provides "date" & "time"
                                            print('A total amount of $' + str(cim) + ' has been refunded.')
                                            cim = 0
                                            print('Thank you for using the vending machine, have a nice day!')
                                            print('\n______________________________________________________\n')
                                            A_Quit = True # "cancels" corresponding loop
                                            L_Category = False # "cancels" corresponding loop
                                            break
                                        elif a in Yes:
                                            A_Quit = True # "cancels" corresponding loop
                                            break
                                        else:
                                            print('\nYour answer "{}" is invalid.'.format(a))
                                            print('\n______________________________________________________\n')
                                            import datetime # current date and time
                                            x = datetime.datetime.now() # inputting current date and time within the variable "x"
                                            print(x) # provides "date" & "time"
                                            print('A total amount of $' + str(cim) + ' has been refunded.')
                                            cim = 0
                                            print('Thank you for using the vending machine, have a nice day!')
                                            print('\n______________________________________________________\n')
                                            A_Quit = True # "cancels" corresponding loop
                                            L_Category = False # "cancels" corresponding loop
                                            break
                                    else:
                                        print('\nYou have received ' + selected.get('item')) # shows user can "receive" the item
                                        selected['stock'] -= 1 # chosen "item" gets "-1 stock" everytime code activates until vending machine is "Rebooted/Restarted"
                                        cim -= price # "cim" minus the "price" of chosen item = overwritten value of "cim"
                                        print('Cash remaining: $' + str(cim))
                                        print('\nSuggested snack for the item you bought is the "' + random.choice(N_Snacks) + '".') # code "random.choice" takes 1 item from "list" and shows
                                        a = input('Would you like to add another item? (Yes/No): ') # redirects user depending on users "choice"
                                        if a in No:
                                            print('\n______________________________________________________\n')
                                            import datetime # current date and time
                                            x = datetime.datetime.now() # inputting current date and time within the variable "x"
                                            print(x) # provides "date" & "time"
                                            print('A total amount of $' + str(cim) + ' has been refunded.')
                                            cim = 0
                                            print('Thank you for using the vending machine, have a nice day!')
                                            print('\n______________________________________________________\n')
                                            A_Quit = True # "cancels" corresponding loop
                                            L_Category = False # "cancels" corresponding loop
                                            break
                                        elif a in Yes:
                                            A_Quit = True # "cancels" corresponding loop
                                            break
                                        else:
                                            print('\nYour answer "{}" is invalid.'.format(a))
                                            print('\n______________________________________________________\n')
                                            import datetime # current date and time
                                            x = datetime.datetime.now() # inputting current date and time within the variable "x"
                                            print(x) # provides "date" & "time"
                                            print('A total amount of $' + str(cim) + ' has been refunded.')
                                            cim = 0
                                            print('Thank you for using the vending machine, have a nice day!')
                                            print('\n______________________________________________________\n')
                                            A_Quit = True # "cancels" corresponding loop
                                            L_Category = False # "cancels" corresponding loop
                                            break
                        else:
                            print('ERROR: Sorry, that item is not available. Please select another item.')
                            continue
                else:
                    print('The given input "{}" is invalid.'.format(Category))
                    print()
                    Proceed = input('Do you still wish to proceed (Yes/No): ')
                    if Proceed in Yes:
                        print()
                        continue
                    elif Proceed in No:
                        print('\n______________________________________________________\n')
                        import datetime # current date and time
                        x = datetime.datetime.now() # inputting current date and time within the variable "x"
                        print(x) # provides "date" & "time"
                        print('A total amount of $' + str(cim) + ' has been refunded.')
                        cim = 0
                        print('Thank you for using the vending machine, have a nice day!')
                        print('\n______________________________________________________\n')
                        L_Category = False # "cancels" corresponding loop
                    else:
                        print('The given input "{}" is invalid.'.format(Proceed))
                        print('\n______________________________________________________\n')
                        import datetime # current date and time
                        x = datetime.datetime.now() # inputting current date and time within the variable "x"
                        print(x) # provides "date" & "time"
                        print('A total amount of $' + str(cim) + ' has been refunded.')
                        cim = 0
                        print('Thank you for using the vending machine, have a nice day!')
                        print('\n______________________________________________________\n')
                        L_Category = False # "cancels" corresponding loop
        elif query in No:
            print('Come again next time, have a nice day!\n')
            print()
            continue
        else:
            print('Your answer "{}" is invalid.'.format(query))
            print()
            continue
vend()