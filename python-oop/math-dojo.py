# Create a Python class called MathDojo that has the methods add and subtract.
class MathDojo(object):
    def __init__(self):
        self.sum = 0

    def add(self, *args):
        for arg in args:
            if type(arg) is list:
                self.sum += sum(arg)
            elif type(arg) is tuple:
                for i in arg:
                    self.sum += i
            else:
                self.sum += arg
        return self

    def subtract(self, *args):
        for arg in args:
            if type(arg) is list:
                self.sum -= sum(arg)
            elif type(arg) is tuple:
                for i in arg:
                    self.sum -= i
            else:
                self.sum -= arg
        return self

    def result(self):
        print self.sum

#md.add(2).add(2,5).subtract(3,2).result, which should perform 0+2+(2+5)-(3+2) and return 4
MathDojo().add(2).add(2,5).subtract(3,2).result()
MathDojo().add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()
MathDojo().add((1, 2),(1,3),5).subtract(2, [2,3], [1.1,2.3], (1,5,6)).result()
