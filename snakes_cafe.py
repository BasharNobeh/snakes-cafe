
if __name__ == "__main__" : 


    our_menu = ("Wings", "Cookies" , "Spring Rools" ,"Salmon", "Steak", "Meat Tornado", "A literal Garden",
    "Ice Cream", "Cake", "Pie" , "Coffee", "Tea", "Unicorn Tears")

    MENU = ''' 
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************

    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears

    ***********************************
    ** What would you like to order? **
    ***********************************
    '''
    user_order = {}

    print(MENU)
    while True : 
        order = input("> ")
        if order in our_menu:
            user_order[order] = user_order.get(order,0)+1

                    
            print("** " , end = "")
            for meal in user_order:
                
                if user_order[meal] == 1:
                    print(f"1 order of {meal} ", end="")
                elif user_order[meal] > 1:  
                    print(f"{user_order[meal]} orders of {meal} ", end="")  
            print("Has been added to your meal **")

                
            
        elif order == "quit":
            if len(user_order) == 0:
                print("Have a nice Day !")
            else :
                    print("You ordered : ")
            for meal in user_order:
                print(user_order[meal] , meal)
                

            
            break

        else :
            print(f"****************\nCould not find {order} :( \nWe will do our best to provide it next time <3\nHave a nice day.\nYou can now continue ordering from our menu\n****************")
            print("# Things you ordered till now :  ")
            for meal in user_order:
                print(user_order[meal] , meal)        






