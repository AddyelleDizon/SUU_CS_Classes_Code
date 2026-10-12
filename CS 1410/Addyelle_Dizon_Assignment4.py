from abc import ABC, abstractmethod
from vehicle_factory import *

class Manufacturer(ABC):
    @abstractmethod
    def create_car(self):
        pass

    @abstractmethod
    def create_truck(self):
        pass

    @abstractmethod
    def create_suv(self):
        pass

class Vehicle_Factory():
    def __init__(self, manufacturer=Manufacturer):
        self.manufacturer = manufacturer

    def create_car(self):
        return self.manufacturer.create_car()

    def create_truck(self):
        return self.manufacturer.create_truck()

    def create_suv(self):
        return self.manufacturer.create_suv()

#Abstract Car Types
class Car(ABC):
    @abstractmethod
    def print_car(self):
        pass

class Truck(ABC):
    @abstractmethod
    def print_truck(self):
        pass

class SUV(ABC):
    @abstractmethod
    def print_suv(self):
        pass

#Honda Types
class Honda_Car(Car):
    def print_car(self):
        print("Honda Accord")

class Honda_Truck(Truck):
    def print_truck(self):
        print("Honda Ridgeline")

class Honda_SUV(SUV):
    def print_suv(self):
        print("Honda CRV")

#Chevy Types
class Chevy_Car(Car):
    def print_car(self):
        print("Chevy Impala")

class Chevy_Truck(Truck):
    def print_truck(self):
        print("Chevy Silverado")

class Chevy_SUV(SUV):
    def print_suv(self):
        print("Chevy Suburban")

#Telsa Types
class Tesla_Car(Car):
    def print_car(self):
        print("Tesla Model 3")

class Tesla_Truck(Truck):
    def print_truck(self):
        print("Tesla Cybertruck")

class Tesla_SUV(SUV):
    def print_suv(self):
        print("Tesla Model X")

#Honda Manufacturer
class Honda(Manufacturer):
    def create_car(self):
        return Honda_Car()

    def create_truck(self):
        return Honda_Truck()

    def create_suv(self):
        return Honda_SUV()

#Chevy Manufacturer
class Chevy(Manufacturer):
    def create_car(self):
        return Chevy_Car()

    def create_truck(self):
        return Chevy_Truck()

    def create_suv(self):
        return Chevy_SUV()

#Tesla Manufacturer
class Tesla(Manufacturer):
    def create_car(self):
        return Tesla_Car()

    def create_truck(self):
        return Tesla_Truck()

    def create_suv(self):
        return Tesla_SUV()

def main():
    print("Welcome to the Auto Selector \nPlease choose a brand: \n 1. Chevy \n 2. Honda \n 3. Tesla")
    choiceBrand = int(input("I would like a: "))

    match choiceBrand:
        case 1:
            manufacturer = Chevy()
        case 2:
            manufacturer = Honda()
        case 3:
            manufacturer = Tesla()
        case default:
            print("Please choose a valid option.")
            return

    vehicle_factory = Vehicle_Factory(manufacturer)

    print("Please choose a type: \n 1. Car \n 2. Truck \n 3. SUV")
    choiceType = int(input("I would like a: "))

    vehicle = None
    match choiceType:
        case 1:
            vehicle = vehicle_factory.create_car()
            vehicle.print_car()
        case 2:
            vehicle = vehicle_factory.create_truck()
            vehicle.print_truck()
        case 3:
            vehicle = vehicle_factory.create_suv()
            vehicle.print_suv()
        case default:
            print("Please choose a valid option.")
            return

if __name__ == "__main__":
    main()
