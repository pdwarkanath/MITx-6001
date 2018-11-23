"""
A catering company has hired you to help with organizing and preparing customer's orders. You are given a list of each customer's desired items, and must write a program that will count the number of each items needed for the chefs to prepare. The items that a customer can order are: salad, hamburger, and water.

Write a function called item_order that takes as input a string named order. The string contains only words for the items the customer can order separated by one space. The function returns a string that counts the number of each item and consolidates them in the following order: salad:[# salad] hamburger:[# hambruger] water:[# water]

If an order does not contain an item, then the count for that item is 0. Notice that each item is formatted as [name of the item][a colon symbol][count of the item] and all item groups are separated by a space.

For example:

If order = "salad water hamburger salad hamburger" then the function returns "salad:2 hamburger:2 water:1"
If order = "hamburger water hamburger" then the function returns "salad:0 hamburger:2 water:1"

"""

def item_order(order):
    '''
    This function takes an order of lower case strings which has 3 items - salad, hamburger and water
    It returns the count of each item in 
    '''
    def countItem(order,item):
        '''
        This function counts the number of times an item appears in an order
        order and item are both strings  in lower case
        Warning: This function uses recursion
        '''
        if item in order:                                             
            return 1 + countItem(order[order.index(item)+1:],item)    #If item exists in order, add 1 to count and look for next instance starting from second letter of first instance
        else:
            return 0
    
    item1 = 'salad'
    item2 = 'hamburger'
    item3 = 'water'
    
    return item1 + ':' + str(countItem(order,item1)) + ' ' + item2 +':' + str(countItem(order,item2)) + ' ' + item3 + ':' + str(countItem(order,item3))

