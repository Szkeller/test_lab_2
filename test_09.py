# FizzBuzz puzzle

class FizzBuzz():
    def __init__(self, number):
        self.number = number
    def fizzbuzz(self):
        if self.number%3== 0 and self.number%5==0:
            return "FizzBuzz"
        elif self.number%3==0:
            return "Fizz"
        elif self.number%5==0:
            return "Buzz"
        else:
            return self.number

if __name__ == "__main__":
    fb = FizzBuzz
    for i in range(1,101):
        print(fb(i).fizzbuzz())