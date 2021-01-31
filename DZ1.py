from itertools import cycle
from time import sleep

class TrafficLight:
    __color = []

    def running(self):
        self.__color = ['Красный', 'Желтый', 'Зеленый']
        i = 0
        for el in cycle(self.__color):
            if (i > 6):
                break
            print(el)
            if (el == 'Красный'):
                sleep(7)
            elif (el == 'Желтый'):
                sleep(2)
            elif (el == 'Зеленый'):
                sleep(15)
            i += 1

TrafficLight = TrafficLight()
TrafficLight.running()


