import decimal

final_cost = decimal.Decimal(31.0025)
final_cost = final_cost.quantize(decimal.Decimal(0.01)), rounding=decimal.ROUND_HALF_UP
