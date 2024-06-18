from pywebio.input import textarea, select, checkbox, radio, FLOAT, DATE, PASSWORD, DATETIME, input as input_pw, slider
from pywebio.output import put_success, put_error, put_warning, put_image, put_html
from pywebio.session import run_js
from pywebio import start_server

admin_one_login = 'itadori'
admin_one_password = 'todo123'

bad_weather = ['Хмарно', 'Шторм']
good_weather = ['Сонячно', 'Сніжно']
weather_options = bad_weather + good_weather

monitoring_info = []

emotions = ['Круто', 'Грустно']


def main():
    put_html('<h1>Мониторимо погоду разом!</h1>')
    # login = input_pw('Ввведіть вваш логін', required=True)
    # password = input_pw('Ввведіть ваш пароль', type=PASSWORD, required=True)
    # if login != admin_one_login or password != admin_one_password:
    #     put_error('Невірний логін або пароль. Сонячної погоди вам!')
    #     run_js('setTimeout(function(){location.reload();}, 3000)')
    #     return

    monitoring_date = input_pw('Поставте дату спостереження', type=DATETIME)
    weather = select('Яка сьогодні погода?', options=['Сонячно', 'Хмарно', 'Шторм'])

    if weather in good_weather:
        put_success('Іди гуляти, не сиди вдома')
    if weather in bad_weather:
        put_error('Краще посидити вдома...')

    short_deskription = textarea('Опишіть яка природа вас оточує')
    temperature = slider('Температура', min_value=-35, max_value=50)
    your_emotions = checkbox('Які у вас емоції?', options=emotions)
    alone = radio('Ви були самі?', options=['Так', 'Ні'])
    if alone == 'Ні':
        put_image(
            'https://www.google.com/url?sa=i&url=https%3A%2F%2Fneurosciencenews.com%2Flonely-alone-psychology-25140%2F&psig=AOvVaw3MIjxuYhfCzEdFkN_NwU0d&ust=1718128917701000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCKi1tZDP0YYDFQAAAAAdAAAAABAE')
    else:
        put_image('https://miro.medium.com/v2/resize:fit:1400/0*L0-D_iSrqx7M8TAr.jpg')
    monitoring_info.append([monitoring_date, weather])
    run_js('setTimeout(function(){location.reload();}, 6000)')


if __name__ == '__main__':
    start_server(main, port=1000)
