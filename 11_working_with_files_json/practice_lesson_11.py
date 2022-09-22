import json
from pprint import pprint


def add_new_entries():
    first_name = input('first name: ').title()
    last_name = input('last name: ').title()
    full_name = last_name + ' ' + first_name
    telephone_number = input('telephone number: ')
    city_or_state = input('city or state: ').title()

    user_info = {'first name': first_name,
                 'last name': last_name,
                 'full name': full_name,
                 'telephone number': telephone_number,
                 'city or state': city_or_state,
                 }

    with open('Phonebook.json', 'r') as file:
        loaded_file = json.load(file)
        loaded_file.append(user_info)

        with open('Phonebook.json', 'w') as file2:
            json.dump(loaded_file, file2, indent=4)


# add_new_entries()


def search_by_first_name():
    user_name = input('contact first name: ').title()

    with open('Phonebook.json', 'r') as file:
        loaded_file = json.load(file)

        for item in loaded_file:
            if item['first name'] == user_name:
                pprint(item)


# search_by_first_name()


def search_by_last_name():
    user_last_name = input('contact last name: ').title()

    with open('Phonebook.json', 'r') as file:
        loaded_file = json.load(file)

        for item in loaded_file:
            if item['last name'] == user_last_name:
                pprint(item)


# search_by_last_name()


def search_by_full_name():
    print('type first and last name')
    first_name = input('first name: ').title()
    last_name = input('last name: ').title()
    full_name = last_name + ' ' + first_name

    with open('Phonebook.json', 'r') as file:
        loaded_file = json.load(file)

        for item in loaded_file:
            if item['full name'] == full_name:
                pprint(item)


# search_by_full_name()


def search_by_telephone_number():
    telephone_number = input('telephone number: ')

    with open('Phonebook.json', 'r') as file:
        loaded_file = json.load(file)

        for item in loaded_file:
            if item['telephone number'] == telephone_number:
                pprint(item)


# search_by_telephone_number()


def search_by_city_or_state():
    city_or_state = input('city or state: ').title()

    with open('Phonebook.json', 'r') as file:
        loaded_file = json.load(file)

        for item in loaded_file:
            if item['city or state'] == city_or_state:
                pprint(item)


# search_by_city_or_state()


def delete_a_record_for_a_given_telephone_number():
    telephone_number = input('telephone number for delete: ')

    with open('Phonebook.json', 'r+') as file:
        loaded_file = json.load(file)

        for item in loaded_file:
            if item['telephone number'] == telephone_number:
                del item


# delete_a_record_for_a_given_telephone_number()


def update_a_record_for_a_given_telephone_number():
    telephone_number = input('telephone number for update: ')

    with open('Phonebook.json', 'r+') as file:
        loaded_file = json.load(file)

        for item in loaded_file:
            if item['telephone number'] == telephone_number:
                del item


def an_option_to_exit_the_program():
    exit()
