name_for_userid = {
    382: 'Элис',
    950: 'Боб',
    590: 'Дилберт',
}

def greetings(user_id):
    return f'Привет {name_for_userid.get(user_id, "всем")}!'
