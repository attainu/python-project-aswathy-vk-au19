import datetime                    
import os
list_foods = []                    
list_drinks = []                   
list_services = []  
list_price = []

def Main():
    while True:
        print("*" * 28 + "FOOD ORDERING SYSTEM" + "*" * 24 + "\n") 
        print("*" * 31 + "MAIN MENU" + "*" * 32 + "\n"     
              "\t(O) ORDER\n"                              
              "\t(P) PAYMENT\n"
              "\t(E) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Operation: ")).upper()    
        if (len(input_1) == 1):                                           
            if (input_1 == 'O'):                                          
                print("\n" * 10)                                        
                def_order_menu()                                          
                break                                                     
            elif (input_1 == 'R'):                                        
                print("\n" * 10)                                        
                def_report()                                              
                break                                                     
            elif (input_1 == 'P'):                                        
                print("\n" * 10)                                         
                def_payment()                                             
                break                                                     
            elif (input_1 == 'E'):                                        
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")           
                break                                                     
            else:                                                                                 
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")     
        else:                                                                                     
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")  
def def_order_menu():                                                                               
    while True:                                             
        print("*" * 31 + "ORDER PAGE" + "*" * 31 + "\n"    
              "\t(F) FOODS AND DRINKS\n"
              "\t(O) OTHER SERVICES\n"
              "\t(M) MAIN MENU\n"
              "\t(E) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Operation: ")).upper() 
        if len(input_1) == 1:
            if (input_1 == 'F'):  
                print("\n" * 10)
                def_food_drink_order()
                break
            elif (input_1 == 'O'):
                print("\n" * 10)
                def_other_services() 
                break
            elif (input_1 == 'M'):
                print("\n" * 10)
                def_main() 
                break
            elif (input_1 == 'E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!") 
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
def def_food_drink_order():
    while True:
            print("*" * 26 + "ORDER FOODS & DRINKS" + "*" * 26)
            print(" |NO| |FOOD NAME|         |PRICE|   |  |NO| |DRINK NAME|        |PRICE|")
            print(  "1    Biryani             120           1      Cock              35")
            print("  2    Roti                 20           1       Sprite           40")
            print("  3    Fried Rice           100          1       Juice            35")
            
            items = int(input("Please select number items: "))
            for i in range (0, items):
                element = input("Enter items from the list: ")
                list_foods.append(element)
                if(element == "Biryani" or element =="Biryani"):
                    list_price.append(120)
                if(element == "Roti" or element =="roti"):
                    list_price.append(20)
                   # list_foods.append(element)
                if(element == "Fried Rice" or element =="fried rice"):
                    list_price.append(100)
                    #list_foods.append(element)
            print("You have selected items of ",list_foods)
            
           

            print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)

            input_1 = input("Please Select Your Operation: ").upper() 
            if (input_1 == 'M'):
                print("\n" * 10)
                def_main() 
                break
            if (input_1 == 'E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n") 
                break
            if (input_1 == 'P'):
                print("\n" * 10)
                def_payment() 
                break
            try:        
                int(input_1)
                if ((int(input_1) <= len(list_foods) and int(input_1) > 0) or (int(input_1) <= len(list_drinks) + 40 and int(input_1) > 40)):
                     try:
                        print("\n" + "_" * 72 + "\n" + str(list_foods[int(input_1) - 1])) 
                     except:
                        pass
                     try:
                         print("\n" + "_" * 72 + "\n" + str(list_drinks[int(input_1) - 41])) 
                     except:
                        pass

                     input_2 = input("How Many You Want to Order?: ").upper() 
                     if int(input_2) > 0:
                        list_item_order[int(input_1) - 1] += int(input_2) 
                        print("\n" * 10)
                        print("Successfully Ordered!")
                        def_food_drink_order() 
                        break
                     else:
                        print("\n" * 10 + "ERROR: Invalid Input (" + str(input_2) + "). Try again!")
            except:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
def def_other_services():
    while True:
        print("*" * 29 + "OTHER SERVICES" + "*" * 29)
        print(" |NO| |SERVICE NAME|      |PRICE|")  
        print ("|1|  |Special music|     |15 |")
        print(" |2|  |Calling taxi|      |35 |")

        items_1 = int(input("Please select number services: "))
        for j in range (0, items_1):
            element_1 = input("Enter service from the list: ")
            list_services.append(element_1)
                
        print("You have selected services of ",list_services)

        print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)

        input_1 = input("Please Select Your Operation: ").upper()
        if (input_1 == 'M'):
            print("\n" * 10)
            def_main() 
            break
        if (input_1 == 'E'):
            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
            break
        if (input_1 == 'P'):
            print("\n" * 10)
            def_payment() 
            break
        try:
            int(input_1)
            if (int(input_1) > 80) and (int(input_1) < 100):
                print("\n" * 10)
                print("Successfully Ordered: " + str(list_services[int(input_1) - 81])) 
                list_item_order[int(input_1) - 1] = 1
                def_other_services()
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
        except:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

def def_payment():
    #while True:
    print("*" * 32 + "PAYMENT" + "*" * 33 + "\n") 
    total_price = 0 
    report_new = "\n\n\n" + " " * 17 + "*" * 35 + "\n" + " " * 17 + "DATE: " + str(datetime.datetime.now())[:19] + "\n" + " " * 17 + "-" * 35 #building up report string header
    print(report_new)
    if 'Special music' in list_services and 'Calling taxi' in list_services:
        print("|Item Name    |  |Price  |")
        print(" Special music           15")
        print ("Calling taxi            35")
        print("Total                    45")
    elif 'Special music' in list_services:
        print("|Item Name    |  |Price  |")
        print(" Special music           15")
        print("Total                    15")
    elif 'Calling taxi' in list_services:
        print("|Item Name    |  |Price  |")
        print(" Calling taxi           35")
        print("Total                    35")
    
    
    if 'Biryani' in list_foods and 'Roti' in list_foods:
        print("|Item Name    |  |Price  |")
        print(" Biryani           120")
        print(" Roti               20")
        print("Total Price = 140")
        print(" Discount(5%) = 7")
        print(" Tax(18%) = 21.6")
        print(" Final amount = 154.6")
    elif 'Biryani' in list_foods and 'Roti' in list_foods and 'Fried Rice' in list_foods:
        print("|Item Name    |  |Price  |")
        print(" Biryani           120")
        print(" Roti               20")
        print(" Fried Rice         100")
        print("Total Price = 240")
        print(" Discount(5%) = 12")
        print(" Tax(18%) = 43.2")
        print(" Final amount = 271.2")
    elif 'Biryani' in list_foods and 'Fried Rice' in list_foods:
        print("|Item Name    |  |Price  |")
        print(" Biryani           120")
        print(" Fried Rice         100")
        print("Total Price = 220")
        print(" Discount(5%) = 11")
        print(" Tax(18%) = 39.6")
        print(" Final amount = 248.6")
    elif 'Roti' in list_foods and 'Fried Rice' in list_foods:
        print("|Item Name    |  |Price  |")
        print(" Roti               20")
        print(" Fried Rice         100")
        print("Total Price = 120")
        print(" Discount(5%) = 6")
        print(" Tax(18%) = 21.6")
        print(" Final amount = 135.6")
    elif 'Biryani' in list_foods:
        print("|Item Name    |  |Price  |")
        print(" Biryani           120")
        print("Total Price = 120")
        print(" Discount(5%) = 6")
        print(" Tax(18%) = 21.6")
        print(" Final amount = 135.6")

Main() 