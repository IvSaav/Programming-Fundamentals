'''
BUDGETING

'''


def sort_rule(x):
    return x[1]


def budgeting(budget, products, wishlist):
    
    # sorted product dictionary (descending order)
    sort_prod = sorted(products.items(), key = sort_rule, reverse = True)
    sort_p = dict(sort_prod)
    
    price_list = list(sort_p.keys())
    total = 0
    for item in price_list:
        if item in wishlist:
            total += sort_p[item] * wishlist[item]
            while(total > budget):
                total -= sort_p[item]
                wishlist[item] -= 1
            if wishlist[item] == 0:
                del wishlist[item]
                
    return wishlist
