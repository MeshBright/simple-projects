def purchased_food_items(item, list=None):
    if list is None:
        list = []
    list.append(item)
    return list

shopping_bag_1 = purchased_food_items("Apple")

print(purchased_food_items("Orange", shopping_bag_1))