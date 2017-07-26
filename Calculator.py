
class Calculator(object):

    def multiplicate(self, a, b):
        return a*b

    def evaluate(self, string):
        '''
        Считает результат арифметических операций в строке, элементы, которой разделены пробелами
        '''
        arr = string.split()
        while arr.count('/') != 0:
            i = arr.index('/')
            divided_digit = 1 / float(arr[i+1])
            arr[i: i+2] = ['*', divided_digit]
            # print(arr)
        while arr.count('*') != 0:
            i = arr.index('*')
            multiplicated = self.multiplicate(float(arr[i-1]), float(arr[i+1]))
            arr[i - 1: i+2] = [multiplicated]
            # print(arr)
        while arr.count('-') != 0:
            i = arr.index('-')
            negative_number = - float(arr[i+1])
            arr[i: i+2] = ['+', negative_number]

        digits = list(filter(lambda x: x != '+', arr))
        digits = list(map(lambda x: float(x), digits))
        return round((sum(digits)), 5)


calculator = Calculator()
print(Calculator().evaluate("2 / 2 + 3 * 4 / 2 - 6 + 2 + 10 / 2"))
