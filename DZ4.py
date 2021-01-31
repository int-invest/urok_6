class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name}'

    def stop(self):
        return f'Машина {self.name} остановилась'

    def turn_left(self):
        return f'Машина {self.name} повернула налево'

    def turn_right(self):
        return f'Машина {self.name} повернула направо'

    def show_speed(self):
        return f'Скорость автомобиля {self.name} {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print("Машина TownCar")

    def show_speed(self):
        print(f'Скорость машины {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} км/ч выше разрешенной скорости для {self.name}'
        else:
            return f'Скорость {self.name} км/ч нормальная скорость для {self.name} '

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print("Машина SportCar")

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print("Машина WorkCar")

    def show_speed(self):
        print(f'Скорость машины {self.name} составляет {self.speed} км/ч')

        if self.speed > 40:
            return f'Скорость {self.name} {self.speed} км/ч выше разрешенной скорости для {self.name}'
        else:
            return f'Скорость {self.name} {self.speed} км/ч нормальная скорость для {self.name} '

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print("Машина PoliceCar")

    def police(self):
        if self.is_police:
            return f'{self.name} Машина полицейская'
        else:
            return f'{self.name} Машина не полицейская'

bmw = SportCar(80, 'Черный', 'BMW', True)
opel = TownCar(25, 'Серый', 'Opel', False)
mazda = WorkCar(64, 'Белый', 'Mazda', True)
reno = PoliceCar(110, 'Желтый',  'Reno', True)
mersedes = Car(70, 'Черный', 'Mersedes', False)

print(opel.turn_left())
print(bmw.show_speed())
print(mazda.show_speed())
print(reno.police())
print(reno.show_speed())
print(mersedes.show_speed())
print(f'{opel.turn_right()}, а {bmw.stop()}')
print(f'{mazda.go()} поехала со скоростью {mazda.show_speed()} км/ч')
print(f'{mersedes.name}  {mersedes.color}')
