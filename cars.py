import os
import csv


class BaseCar:
    def __init__(self, car_type, photo_file_name, brand, carrying):
        self.car_type = car_type
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1][1:]


class Car(BaseCar):
    def __init__(self, photo_file_name, brand, carrying, passenger_seats_count):
        super(Car, self).__init__("car", photo_file_name, brand, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(BaseCar):
    def __init__(self, photo_file_name, brand, carrying, body_width, body_height, body_length):
        super(Truck, self).__init__("truck", photo_file_name, brand, carrying)
        self.body_width = body_width
        self.body_height = body_height
        self.body_length = body_length

    def get_body_volume(self):
        return self.body_height * self.body_length * self.body_width


class SpecMachine(BaseCar):
    def __init__(self, photo_file_name, brand, carrying, extra):
        super(SpecMachine, self).__init__("spec_machine", photo_file_name, brand, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            car = None
            try:
                car_type = row[0]
                brand = row[1]
                photo = row[3]
                carry = row[5]

                if car_type == "car":
                    car = Car(photo, brand, carry, int(row[2]))
                elif car_type == "truck":
                    size = row[4].split('x')
                    if len(size) < 3:
                        w = 0.0
                        h = 0.0
                        le = 0.0
                    else:
                        w = float(size[1])
                        h = float(size[2])
                        le = float(size[0])

                    car = Truck(photo, brand, carry, w, h, le)
                elif car_type == "spec_machine":
                    car = SpecMachine(photo, brand, carry, row[6])

            except Exception:
                print("row was skipped. row: {}".format(row))
            else:
                car_list.append(car)

    return car_list


if __name__ == "__main__":
    print(get_car_list("coursera_week3_cars.csv"))
