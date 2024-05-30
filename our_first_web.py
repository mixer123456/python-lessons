from pywebio.input import input as input_pw
from pywebio.input import NUMBER
from pywebio.output import put_text, put_html, put_image


import constans_web

# pizza_cost = 250
# cola_cost = 60
# msg_enter_quantity = 'Enter the desired quantity'
# msg_ask_name = 'How your name?'

# header
put_html('<h1>Welcome to Freedy Fazbear Pizza</h1>')
put_html('<h2>Make order 🍕</h2>')

# input section
name = str(input_pw(constans_web.msg_ask_name)).title()

formatted_name = f'Good day, {name}! How many promotional pizzas will you order?'
put_text(formatted_name)

pizza_count_order = input_pw(f'{constans_web.msg_enter_quantity} of pizzas', type=NUMBER)
pizza_order_cost = pizza_count_order * constans_web.pizza_cost

formatted_order_cola = f'{name}, I still highly recommend a coke {constans_web.cola_cost} UAH for bottle'
put_text(formatted_order_cola)
cola_count_order = input_pw(f'{constans_web.msg_enter_quantity} colas', type=NUMBER)
cola_order_cost = cola_count_order * constans_web.cola_cost

total_cost = pizza_order_cost + cola_order_cost
formatted_total_cost = f'From you {total_cost} UAH'
put_text(formatted_total_cost)

img = open('pizza.avif', 'rb').read()
put_image(img, width='500px')
