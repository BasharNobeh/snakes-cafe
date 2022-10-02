


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
order_list = []
print(MENU)
while True : 
    order = input("> ")
    if order in our_menu:
        user_order[order] = user_order.get(order,0)+1

             

        for meal in user_order:
            if user_order[meal] == 1:
                print(f"1 order of {meal} ", end="")
            elif user_order[meal] > 1:  
                print(f"{user_order[meal]} orders of {meal} ", end="")  
        print("Has been added to your meal")

           
      
    elif order == "quit":
        print("Your ordered : ")
        for meal in user_order:
            print(user_order[meal] , meal)
            
        break
    
    else :
        print(f"Could not find {order} :( \nWe will do our best to provide it next time <3\nHave a nice day.\nYou can now continue ordering from our menu")
        print("# Things you ordered till now :  ")
        for meal in user_order:
            print(user_order[meal] , meal)        


# for item in order:





