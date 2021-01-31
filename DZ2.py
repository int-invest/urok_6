class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass_road(self, m_depth1, depth):
        mass = (self.__length * self.__width * m_depth1 * depth) / 1000
        print(f'Необходимо {mass} тонн асфальта')


road = Road(15000, 10)
road.mass_road(27, 3)

