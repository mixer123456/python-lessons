from constants import MSG_INPUT_FIRST_NAME, MSG_INPUT_LAST_NAME

user_first_name = input(MSG_INPUT_FIRST_NAME).title().strip()
# user_first_name = user_first_name.title()
# user_first_name = user_first_name.strip()
user_last_name = input(MSG_INPUT_LAST_NAME).title().strip()
# user_last_name = user_last_name.title()
# user_last_name = user_last_name.strip()

print(user_first_name)
print(user_last_name)

welcome_text = 'welcome to the our game, '

# гарніше буде 
# <назва змінної> = f'якийсь текс'
# template = 'welcome to the our game,  {first_name} {last_name}!'
# result = template.format(first_name=user_first_name, last_name=user_last_name)

result = f'welcome to the our game,  {user_first_name} {user_last_name}!'

print(result)
