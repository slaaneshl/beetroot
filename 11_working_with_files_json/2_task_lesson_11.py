import module_2_lesson_11

print("Extend Phonebook application\n"
      "1. Add new entries\n"
      "2. Search by first name\n"
      "3. Search by last name\n"
      "4. Search by full name\n"
      "5. Search by telephone number\n"
      "6. Search by city or state\n"
      "7. Delete a record for a given telephone number\n"
      "8. Update a record for a given telephone number\n"
      "9. An option to exit the program\n")

while True:
    option = input('Choice option: ')

    if option == '1':
        module_2_lesson_11.add_new_entries()

    if option == '2':
        module_2_lesson_11.search_by_first_name()

    if option == '3':
        module_2_lesson_11.search_by_last_name()

    if option == '4':
        module_2_lesson_11.search_by_full_name()

    if option == '5':
        module_2_lesson_11.search_by_telephone_number()

    if option == '6':
        module_2_lesson_11.search_by_city_or_state()

    if option == '7':
        module_2_lesson_11.delete_a_record_for_a_given_telephone_number()

    if option == '8':
        module_2_lesson_11.update_a_record_for_a_given_telephone_number()

    if option == '9':
        module_2_lesson_11.an_option_to_exit_the_program()