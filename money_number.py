import decimal

cheese_kg = decimal.Decimal('0.235')
cheese_price = decimal.Decimal('133.33').quantize(decimal.Decimal('0.01'))

final_cost = cheese_kg * cheese_price
final_cost = final_cost.quantize(decimal.Decimal('0.01')), rounding = decimal.ROUND_HALF_UP
print(final_cost)

# represintation
divider_symbol = '-'
divider = divider_symbol * 30
cheese_emoji = '\U0001F9C0'
shop_name = 'ATB'`
header = f'{divider} {shop_name} {divider}'
len_header = len(header)
footer = divider_symbol * len_header
print(header)
print('Goods\t\t\tweigh\t\t\tprice')
print(f'cheese\t\t\t{cheese_kg}\t\t\t{cheese_price}\t\t\t{final_cost}')
print(footer)
