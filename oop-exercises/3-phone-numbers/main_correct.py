import csv
import sys
from person import Person


def open_csv(file_name):
    people = []
    with open(file_name) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            people.append(Person(row[0], row[1]))
    return people


def get_csv_file_name(argv_list):
    if len(argv_list) > 1:
        return argv_list[1]
    return None


def format_output(person):
    if person is not None:
        return 'This number belongs to: ' + person.get_name()
    return 'No match found.'


def get_person_by_phone_number(person_list, user_input_phone_number):
    for person in person_list:
        if person.is_phone_number_matching(user_input_phone_number):
            return person
    return None


def main():
    file_name = get_csv_file_name(sys.argv)
    if file_name is None:
        print('No database file was given.')
        sys.exit(0)

    person_list = open_csv(file_name)
    user_input_phone_number = input('Please enter the phone number: ')
    match_person = get_person_by_phone_number(person_list, user_input_phone_number)

    print(format_output(match_person))

if __name__ == '__main__':
    main()
