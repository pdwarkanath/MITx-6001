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

