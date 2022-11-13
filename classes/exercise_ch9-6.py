from classes.working_with_classes import *


class User:

    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 2

    def describe_user(self):
        print(f"Full name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age} y.o")
        print(f"Country: {self.country}")

    def greet_user(self):
        print(f"Welcome {self.first_name}, you are now logged in.\n")

    # Write a method called increment_
    # # login_attempts() that increments the value of login_attempts by 1.
    def increment_login_attempts(self, login_attempts):
        """number of login attempts will be incremented by 1"""
        self.login_attempts += login_attempts

    # Write another method called reset_login_attempts() that resets the value of login_
    # # attempts to 0.
    def reset_login_attempts(self):
        """number of login attempts will be set to 0"""
        self.login_attempts = 0


print('\n--------------- 9-8 -----------------\n')


class Privileges:

    def __init__(self):
        self.list_of_privileges = []

    def show_privileges(self):
        """function show_privileges displays admin's set of privileges"""
        print(f"Privileges:")
        if self.list_of_privileges:
            for privilege in self.list_of_privileges:
                print(f"\t{privilege}")
        else:
            print(f"\nNo privileges.")

    def test(self):
        print("Privileges class test")


# class Admin(User, Privileges):
class Admin(User):
    # privileges = Privileges()

    def __init__(self, first_name, last_name, age, country):
        """add attribute privileges that stores a list"""
        super().__init__(first_name, last_name, age, country)
        self.admin_privileges = Privileges()

    def test(self):
        print('Admin test:')


# # Make a Privileges instance as an attribute in the Admin class.
# Create a new instance of Admin and use your method to show its privileges.

admin1 = Admin('jackie', 'jones', 34, 'japan')
admin1.describe_user()
admin1.admin_privileges.show_privileges()

print('\nNew addition ->')
new_privileges = [
    'can override error',
    'can reset account',
    'can moderate comments',
]
# admin1 is the object of Admin class
# admin_privileges is the object inside the Admin class
# list_of_privileges is the attribute inside Privileges class
admin1.admin_privileges.list_of_privileges = new_privileges

# show_privileges is the method (behaviour) inside Privileges class
admin1.admin_privileges.show_privileges()

# why we need object in the class
admin1.test()
admin1.admin_privileges.test()

# 9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery(). This method
# should check the battery size and set the capacity to 85 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once, and
# then call get_range() a second time after upgrading the battery. You should
# see an increase in the car’s range.

class Battery():

    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def get_range(self):
        """Print a statement about the range this battery provides."""
        range = 0
        if self.battery_size == 70:
            range = 260
        elif self.battery_size == 85:
            range = 310

        # message = f"This car can go approximately {range}"
        # message += " miles on a full charge."
        # print(message)
        print(f'This car can go approximately {range} miles on a full charge. ')

    def upgrade_battery(self):
        if self.battery_size < 85:
            print("your battery is less than national standard you are eligible to free upgrade")
            self.battery_size = 85
            print(f'Battery size upgraded to 85 kwh.')
        else:
            print('Battery size is at the upgraded level.')


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


print("**********************************************")
print('Check the battery of this electric car:')
electric_car1 = ElectricCar('Rivian', 'R1T', 2022)
electric_car1.battery.get_range()

print('\nCheck the upgraded battery of this electric car:')
electric_car1.battery.upgrade_battery()
electric_car1.battery.get_range()
