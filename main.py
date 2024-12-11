import os
import pickle

class Car:
    def __init__(self, license_plate, make, year):
        self.license_plate = license_plate
        self.make = make
        self.year = year

def print_tutorial():
    print("1. Use 'add license_plate Brand year' to add a car to garage")
    print("2. Use 'view license_plate' to view a car from garage")
    print("3. To quit just write 'quit' ")
    print("4. To delete a car from garage write 'delete license_plate'")

with open(os.getcwd() + '/' + 'garage.b', 'rb') as file:
    garage = pickle.load(file)

print_tutorial()

while True:
    user_input = input().split(' ')
    if 'add' in user_input:
        if len(user_input) != 4:
            print("Seems like you've typed in wrong format. Here's a little tutorial: ")
            print_tutorial()
            continue
        car = Car(user_input[1], user_input[2], user_input[3])
        for j in garage:
            i = 0
            if j.license_plate == car.license_plate:
                command = input('This car is already in the garage. Do you want to overwrite it? (Type "yes" or "no"): ').lower()
                if command.lower() != 'yes':
                    print(f'Car {car.license_plate} was not added to garage. Try again.')
                else:
                    garage[i] = Car(user_input[1], user_input[2], user_input[3])
                    print(f'Car {car.license_plate} was successfully added to garage.')
                break
            i += 1
        else:
            garage.append(car)
    elif 'view' in user_input:
        if len(user_input) != 2:
            print("Seems like you've typed in wrong format. Here's a little tutorial: ")
            print_tutorial()
            continue
        for car in garage:
            if car.license_plate == user_input[1]:
                print(f'License plate: {car.license_plate}')
                print(f'Make: {car.make}')
                print(f'Year: {car.year}')
                break
        else:
            print(f'No such car in garage. Try again. Cars in garage: {[car.license_plate for car in garage]}')
    elif 'delete' in user_input:
        if len(user_input) != 2:
            print("Seems like you've typed in wrong format. Here's a little tutorial: ")
            print_tutorial()
            continue
        for car in garage:
            if car.license_plate == user_input[1]:
                command = input('Do you really want to remove this car? THis action is irreversible. (Yes/No): ')
                if command.lower() != 'yes':
                    print(f'Car {car.license_plate} was not deleted from garage. Try again.')
                    break
                garage.remove(car)
                print(f'Car {car.license_plate} was successfully deleted from garage.')
                break
            else:
                print(f'No such car in garage. Try again. Cars in garage: {[car.license_plate for car in garage]}')
                break
    elif 'quit' in user_input:
        with open('garage.b', 'wb') as file:
            pickle.dump(garage, file)
        quit()
    else:
        print("Seems like you've typed in wrong format. Here's a little tutorial: ")
        print_tutorial()


