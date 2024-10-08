class Temperature:

    def __init__(self,celsius):

        self.__celsius = celsius

    def to_faringheit(self):
        return self.__celsius * 9/5 +32

    def get_celsius(self):
        return self.__celsius


temp = Temperature(25)
print(temp.to_faringheit())
print(temp.get_celsius())




