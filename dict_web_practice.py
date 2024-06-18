from pywebio.input import textarea, select, checkbox, radio, FLOAT, DATE, PASSWORD, DATETIME, input as input_pw, slider, \
    input_group
from pywebio.output import put_success, put_error, put_warning, put_image, put_html, put_table
from pywebio.session import run_js
from pywebio import start_server

creds = {
    'login': 'admin',
    'password': '123',
}

observing_data = []


def main():
    put_html('<h1>Мониторимо погоду разом!</h1>')
    # login_form = input_group(
    #     'Enter your creds',
    #     [
    #         input_pw('Login', placeholder='Login here', name='login'),
    #         input_pw('Password', placeholder='Input password here', type=PASSWORD, name='password'),
    #     ]
    # )
    # if login_form == creds:
    #     put_success('Welcome')
    # else:
    #     put_warning('Try againe')
    #     run_js('setTimeout(function(){location.reload();}, 2000)')
    #     return
    weather_data = input_group(
        'Enter your creds',
        [
            input_pw('temp', name='temp', required=True),
            slider('humanity', name='humanity', min_value=0, max_value=100),
        ]
    )
    observing_data.append(weather_data)

    weather_accumulated_date = [ ['Temperature', 'Humanity']  ]
    for observation in observing_data:
        weather_accumulated_date.append(
            [observation['temp'], observation['humanity']]
        )
    put_table(
        [
            [111, 555],
            [111, 555],
        ]
    )
    print(observing)

    run_js('setTimeout(function(){location.reload();}, 2000)')


if __name__ == '__main__':
    start_server(main, port=5000)
