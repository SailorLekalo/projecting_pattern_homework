from abc import abstractmethod
#Это -- Состояние, оно же стейт
#Суть -- изменять поведение методов в зависимости от контекста

class State():
    @abstractmethod
    def mouseClick(self):
        pass

    @abstractmethod
    def spaceClick(self):
        pass

    @abstractmethod
    def ESCClick(self):
        pass

class HoldingGun(State):
    def mouseClick(self):
        print("Стрельба из оружия")
    def spaceClick(self):
        print("Прыжок с оружием")
    def ESCClick(self):
        print("Убирает оружие за пазуху")
class BareHands(State):
    def mouseClick(self):
        print("Удар кулаком")
    def spaceClick(self):
        print("Прыжок")
    def ESCClick(self):
        print("Выход в меню")
class Dying(State):
    def mouseClick(self):
        print("Тянется к солнцу")
    def spaceClick(self):
        print("Издаёт вопль")
    def ESCClick(self):
        print("Умирает окончательно")

class Player:
    stateMachine = None
    def __init__(self):
        self.stateMachine = HoldingGun()
    def mouseClick(self):
        self.stateMachine.mouseClick()
    def spaceClick(self):
        self.stateMachine.spaceClick()
    def ESCClick(self):
        self.stateMachine.ESCClick()
    def switchState(self, state):
        self.stateMachine = state

player = Player()
player.mouseClick()

player.switchState(BareHands())
player.mouseClick()

player.switchState(Dying())
player.mouseClick()