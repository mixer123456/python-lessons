# from pprint import pprint
#
# person_name = 'Elya'
# person_age = 5
#
# person = {
#     'name': 'Elya',
#     'age': 5,
#     'hobbies': [
#         'foodd',
#         'play with toy'
#     ],
#     'address': None,
#
# }
#
#
# address = person.get('address',) or 'Odesa'
# print(address)
#
# print(30 and 0)
#
#
# shipment = {}
# shipment['toy'] = 'small elephant'
# shipment['food'] = '+1 food'
# shipment['food2'] = '+1 food'
# shipment['food3'] = '+1 food'
# shipment['food4'] = '+1 food'
# shipment[5] = 'jyhtfs'
#
#
# pprint(shipment, indent=4)
#
#
# #
# # item_from_shipment = shipment['food']
# # item_from_shipment = shipment['toy']
# # item_from_shipment = shipment.get('5')
# # item_from_shipment = shipment.get('5', 'lkjhgfdsfyui')
# #
# # print(item_from_shipment)
# del shipment[5]
#
# value = shipment.pop('food4')
# print(value)
# shipment.pop('food4', 4)
#
# pprint(shipment, indent=4)


cars = [
    {
        'number': 1,
        'color': 'blue',
        'price': 50.99,
        'features': [
            'jump',
        ]
    },
    {
        'number': 2,
        'color': 'red',
        'price': 300.99,
        'features': [
            'radio',
            'retro'
        ]
    },
    {
        'number': 3,
        'color': 'white',
        'price': 209.99,
        'features': []
    }
]

# for car in cars:
#     print(f'price:\t\t{car["price"]}')
#     print(f'features:\t{car["features"]}')
#     for feature in car.get('features', []):
#         print(feature)
#     print('_' * 50)


my_tuple = 3, 77
print(my_tuple)

value1, value2 = my_tuple

person = {'name': 'Elya', 'age': 5, 'hobbies': ['food', 'play with toy'], 'address': None}

for key, value in person.items():
    print(key, '>>>', value)
    # print(person[item])
    print('_' * 50)

for key in person.keys():
    print(key)
    # print(person[item])
    print('+' * 50)

for kvalue in person.values():
    print(value)
    # print(person[item])
    print('=' * 50)
