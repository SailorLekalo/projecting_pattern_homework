#Это -- Адаптер.
#Его суть -- делать объект одного класса пригодным для обработки функцией, принимающей другие объекты
class Cat:
    name: str
    def __init__(self,name):
        self.name = name
class Dog:
    name: str

    def __init__(self, name):
        self.name = name
class CatGroomer:
    def groom(self,cat: Cat):
        if isinstance(cat,Cat):
            print(f"Кошка {cat.name} вычесана")
        else:
            print(f"{cat.name} -- не кошка!")
class DogToCatAdapter(Cat):
    def __init__(self, dog: Dog):
        self.name = dog.name

cgr = CatGroomer()

billy = Cat("Билли")
alex = Dog("Алекс")

cgr.groom(billy)
cgr.groom(alex)

cgr.groom(DogToCatAdapter(alex))