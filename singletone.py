## Это - синглтон, он же Одиночка.
##Суть -- сделать класс, у которого может быть только один экземпляр.
##Зачем это может быть нужно?
##- Управление подключениями. Например, к базе данных должно быть только одно подключение.
##- Логирование
##
##В чём фишка:
##- Можно всегда создать инстанс класса, и получить объект, ссылающийся именно на тот единственный инстанс


## DeepSeek отметил, что этому коду недостаёт защиты от повторной инициализации и поддержки многопоточности
class Singletone:
    _instance = None
    _init_lock = None
    yay_variable = "something"

    def __new__(self):
        if self._instance is None:
            self._instance = super(Singletone, self).__new__(self)
        return self._instance

    def yay(self):
        return self.yay_variable


# Простейший пример, демонстрирующий функционал синглтона.
a = Singletone()  # мы создаём синглтон а
print(a.yay())


def some_def(i):
    if i == 0:
        return
    else:
        # тут мы всякий раз создаём новый экземпляр, меняем переменную для него
        temp = Singletone()
        temp.yay_variable = i
        # а выводим переменную из экземпляра а
        print(a.yay())
        some_def(i - 1)


some_def(10)


class Tester:
    tone = None

    def __init__(self):
        self.tone = Singletone()

    def return_tone(self):
        return self.tone.yay()


test = Tester()
print(test.return_tone())
