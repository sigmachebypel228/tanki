class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print('Гав-гав!!!')

class BigDog(Dog):
    def speak(self):
        print('Аавв -АВВ!!!')
class SmallDog(Dog):
    def speak(self):
        print('тяф тяф!!!!')
class ToyDog(SmallDog):
    def speak(self):
        print('мяу мяу')
class TermiDog(ToyDog):
    def speak(self):
        print("тьяф тьяф тьяф тьяф I'll be back!!!!")
class AngryBigDog(BigDog):
    def speak(self):
        super().speak()
        print('Хочит откусить руку!!!')
class Cat(Animal):
    def _may(self):
        print('I always come back!')
    def speak(self):
        self._may()
class TOXIC:
    def speak(self):
        print('*Вылезает из помойки*')
class SIMBOCHKA:
    def speak(self):
        print('*Сбивает КАМАЗ*')
tox = TOXIC()
tox.speak()
cat = Cat()
cat.speak()
abd = AngryBigDog()
abd.speak()
ter = TermiDog()
ter.speak()
bdog = BigDog()
sdog = SmallDog()
bdog.speak()
sdog.speak()
animal = Animal()
animal.speak()
dog = Dog()
dog.speak()
tdog = ToyDog()
tdog.speak()
kamazik = SIMBOCHKA()
def say_n_times(animal,times):
    for _ in range(times):
        animal.speak()
chekrushkin = AngryBigDog()
list = [SIMBOCHKA(),ToyDog(),Dog(),SmallDog(),BigDog(),AngryBigDog(),TOXIC()]
for animal in list:
    say_n_times(animal, 1)



