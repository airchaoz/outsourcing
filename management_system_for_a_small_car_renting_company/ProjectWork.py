import datetime


def readtxt(filename):
    result = []
    with open(filename, 'r') as f:
        content = f.read().strip().split('\n')
    for s in content:
        result.append(s.split(','))
    return result


CUSTOMERS = readtxt('Customers.txt')
VEHICLES = readtxt('Vehicles.txt')
RENTEDVEHICLES = readtxt('rentedVehicles.txt')
TRANSACTIONS = readtxt('transActions.txt')


def savetxt():
    with open('Customers.txt', 'w') as f:
        for item in CUSTOMERS:
            f.write(",".join(item))
            f.write('\n')

    with open('Vehicles.txt', 'w') as f:
        for item in VEHICLES:
            f.write(",".join(item))
            f.write('\n')

    with open('rentedVehicles.txt', 'w') as f:
        for item in RENTEDVEHICLES:
            f.write(",".join(item))
            f.write('\n')

    with open('transActions.txt', 'w') as f:
        for item in TRANSACTIONS:
            f.write(",".join(item))
            f.write('\n')


def print_base_menu():
    print("You may select one of the following:")
    print("1) List available cars")
    print("2) Rent a car")
    print("3) Return a car")
    print("4) Count the money")
    print("0) Exit")
    print("What is your selection?")


def list_available_cars():
    rented_vehicles_ids = []
    for item in RENTEDVEHICLES:
        rented_vehicles_ids.append(item[0])

    print("The following cars are available:")
    for item in VEHICLES:
        if item[0] not in rented_vehicles_ids:
            print(
                f"* Reg. nr: {item[0]}, Model: {item[1]}, Price per day: {item[2]}")
            print(f"Properties: {', '.join(item[3:])}")
    print()


def is_vaild_birthday(birthday: str):
    if birthday.count('/') != 2:
        print("The birthday you entered is invalid!")
        return False

    day, month, year = birthday.split('/')
    if not day.isdigit() or not month.isdigit() or not year.isdigit():
        print("The birthday you entered is invalid!")
        return False

    day, month, year = int(day), int(month), int(year)

    if year > 2022:
        print("The year of birthday you entered is invalid!")
        return False

    if year > 2004:
        print("You must be at least 18 to rent a car.")
        return False

    if year < 1922:
        print("You can only rent a car if you are under 100.")
        return False

    if month < 1 or month > 12:
        print("The month of birthday you entered is invalid!")
        return False

    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            print("The day of birthday you entered is invalid!")
            return False

    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 31:
            print("The day of birthday you entered is invalid!")
            return False

    elif month == 2:
        if day < 1 or day > 28:
            print("The day of birthday you entered is invalid!")
            return False

    return True


def is_vaild_email(email):
    if '.' not in email or '@' not in email:
        print("The email you entered is invalid!")
        return False

    return True


def add_customer(birthday):
    first_name = input("please enter your first_name:")
    last_name = input("Please enter your last name:")
    while True:
        email = input("Please enter your email:")
        if not is_vaild_email(email):
            print('The email address you entered is invalid')
            continue
        break
    customer = [birthday, first_name, last_name, email]
    CUSTOMERS.append(customer)
    return customer


def rent_a_car():
    vehicles_id = [item[0] for item in VEHICLES]
    rented_vehicles_ids = [item[0] for item in RENTEDVEHICLES]
    birthdays = [item[0] for item in CUSTOMERS]

    car_id = input("Give the register number of the car your want to rent:")
    if car_id not in vehicles_id:
        print("The number of the car you entered doesn't exist.")
        return

    if car_id in rented_vehicles_ids:
        print("The car has been rented.")
        return

    birthday = input("Please enter you birthday in the form DD/MM/YYYY:")
    if not is_vaild_birthday(birthday):
        return

    if birthday in birthdays:
        first_name = CUSTOMERS[birthdays.index(birthday)][1]
    else:
        first_name = add_customer(birthday)[1]
    print(f"Hello {first_name}")

    date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    record = [car_id, birthday, date]
    RENTEDVEHICLES.append(record)
    print(f"You rented the car {car_id}.\n")
    savetxt()


def return_a_car():
    car_ids = [item[0] for item in VEHICLES]
    vehicles_id = [item[0] for item in VEHICLES]
    rented_vehicles_ids = [item[0] for item in RENTEDVEHICLES]

    car_id = input("Give the register number of the car your want to return:")
    if car_id not in vehicles_id:
        print("The number of the car you entered doesn't exist.")
        return

    if car_id not in rented_vehicles_ids:
        print("The car has not rented.")
        return

    rented_index = rented_vehicles_ids.index(car_id)
    record = RENTEDVEHICLES.pop(rented_index)
    birthday = record[1]
    rent_date = datetime.datetime.strptime(record[2], '%d/%m/%Y %H:%M')
    return_date = datetime.datetime.now()
    rent_date_str = record[2]
    return_date_str = return_date.strftime('%d/%m/%Y %H:%M')
    count_day = int(str((return_date - rent_date).days)) + 1

    car_index = car_ids.index(car_id)
    price = float(VEHICLES[car_index][2])

    action = [car_id, birthday, rent_date_str,
              return_date_str, f"{price * count_day:.2f}"]
    TRANSACTIONS.append(action)
    print(f'The rent lasted {count_day} days and the cost is {price * count_day:.2f} euros')
    savetxt()


def count_the_money():
    total = 0.0
    for item in TRANSACTIONS:
        total += float(item[-1])
    print(f"The total amount of money is {total:.2f} euros.")
    print()


def main():
    while True:
        print_base_menu()
        opt = input()
        if opt == '1':
            list_available_cars()
        elif opt == '2':
            rent_a_car()
        elif opt == '3':
            return_a_car()
        elif opt == '4':
            count_the_money()
        elif opt == '0':
            break


main()