import math

class circle():
    def __init__(self, r):
        '''

        :param r: radius
        '''
        self.radius = r
    def area(self):
        '''

        :return: circle area by redius
        '''
        return math.pi * math.pow(self.radius,2)

if __name__ == "__main__":
    circle1 = circle(3)
    print(circle1.area())