'''
HEROES AND VILLAINS
'''


def fight(heroes, villain):
    
    for dic in heroes:
        if villain["category"] == dic["category"]:
            if villain["health"] > dic["health"]:
                villain["health"] -= round(dic["health"]/2,1)
            else:
                dic["score"] += 1
                return "{} defeated the villain and now has a score of {}".format(dic["name"], dic["score"])
    return "{} prevailed with {}HP left".format(villain["name"], round(villain["health"], 1))


print(fight([{'name': 'Genos', 'health': 3000, 'category': 'S', 'score': 0}, {'name': 'Blizzard of Hell', 'health': 1000, 'category': 'B', 'score': 0}, {'name': 'Saitama', 'health': 9001, 'category': 'C', 'score': 0}, {'name': 'King', 'health': 2000, 'category': 'S', 'score': 1}], {'name': 'Hero Killer', 'health': 4000, 'category': 'S'}))        