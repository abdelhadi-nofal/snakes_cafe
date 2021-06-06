def Menu():
    print("""
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
    """)
  
def enterOrder():
    
    list=["wings", "cookies", "spring rolls","salmon", "steak", "meat tornado", "a literal garden","ice cream", "cake", "pie","coffee", "tea", "unicorn tears"]
    cnt_list=[0, 0, 0,0, 0, 0, 0,0, 0,0,0, 0,0]
    order = input('> ')
    
    while order!="QUIT":
       
       if order.lower() in list:
        
        value =cnt_list[list.index(order)]
        
        value+= 1
        cnt_list[list.index(order)]=value

        print(f'** {value} order of {order} have been added to your meal **')
        
        print("IF YOU FINSIDED PRINT QUIT")
        order =input('> ')

        # continue
       elif order == 'QUIT' or order =='quit':
        exit() 
       elif order not in list:
           print("Try Something from our list")
           order =input('> ')
        
Menu()
enterOrder()
