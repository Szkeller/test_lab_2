
class apple():
    def __init__(self, a, b, c, d):
         self.weight = a
         self.color = b
         self.taste = c
         self.place_of_origin = d

    def print_attr(self):
        """

        :param a:
        :param b:
        :param c:
        :param d:
        """
        print("weight of this apple is {}".format(self.weight))
        print("color of this apple is {}".format(self.color))
        print("taste of this apple is {}".format(self.taste))
        print("plance of origin of this aaple is {}".format(self.place_of_origin))

if __name__ == "__main__":
    Apple = apple(10,'red','sweet','guangdong')

    Apple.print_attr()