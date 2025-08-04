#Это -- фабричный метод.
#Суть паттерна: приведение всех продуктов к единому интерфейсу
#и создание этих продуктов единым методом.
#Он нужен если:
# - Есть несколько вариантов делать одно и то же действие
# Например: "Доставку" можно делать почтой, можно курьером, а можно голубем
# - Мы заранее не знаем, не появится ли ещё варианты и какой вариант нужен клиенту

from abc import abstractmethod
class DeliverType:
    @abstractmethod
    def Deliver(cls):
        pass

class DeliveryFactory:
    def Deliver(self):
        deltype: DeliverType = self.CreateDelivery()
        deltype.Deliver()
    @abstractmethod
    def CreateDelivery(self):
        pass

class AutoDelivery(DeliverType):
    def Deliver(self):
        print("Логика доставки автомобилем")

class ShipDelivery(DeliverType):
    def Deliver(self):
        print("Логика доставки кораблём")

class PlaneDelivery(DeliverType):
    def Deliver(self):
        print("Логика доставки самолётом")
class AutoDeliveryFactory(DeliveryFactory):
    def CreateDelivery(self):
        return AutoDelivery()
class ShipDeliveryFactory(DeliveryFactory):
    def CreateDelivery(self):
        return ShipDelivery()
class PlaneDeliveryFactory(DeliveryFactory):
    def CreateDelivery(self):
        return PlaneDelivery()

preferred_delivery_type = "Plane" #Можно поменять на Auto или Plane

howto_deliver: DeliveryFactory

if preferred_delivery_type == "Ship":
    howto_deliver = ShipDeliveryFactory()
elif preferred_delivery_type == "Plane":
    howto_deliver = PlaneDeliveryFactory()
elif preferred_delivery_type == "Auto":
    howto_deliver = AutoDeliveryFactory()
else:
    print("Неизвестный метод доставки")

howto_deliver.Deliver()