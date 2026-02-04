
from __future__ import annotations

#1
# class Car:
#
#     brand: str
#     model: str
#     realese_year: str
#     color: str
#     mileage: float
#     is_engine_active: bool
#     speed: float
#
#
#     def __init__(self, brand: str, model: str,  realese_year: str, color: str, mileage: float, is_engine_active: bool, speed: float):
#
#         self.brand = brand
#         self.model = model
#         self.release_year = realese_year
#         self.color = color
#         self.mileage = mileage
#         self. is_engine_active = is_engine_active
#         self.speed = speed
#
#
#     def __str__(self):
#         return f"Brand: {self.brand}\nModel: {self.model}\nYear release: { self.release_year}\nColor: {self.color}\nMileage: {self.mileage}\nIs active engine: { self. is_engine_active}\nSpeed: {self.speed}"
#
#     def run_engine(self):
#         self. is_engine_active == True
#
#
#
#     def stop_engine(self):
#         self. is_engine_active == False
#
#
#     def set_increase_speed(self,delta: float):
#         if delta < 0 or delta > 200:
#             return None
#
#         self.speed += delta
#
#
#     def set_decrease_speed(self,delta: float):
#         if delta < 0 or delta > 200:
#             return None
#
#         self.speed -= delta
#
#
#
#     def repainting(self, new_color: str) -> None:
#
#         self.color = new_color
#
#
#     def is_engine_active(self) -> bool:
#         return True if self. is_engine_active else False
#
#     def get_speed(self):
#         return self.speed
#
#     def get_mileage(self):
#         return self.mileage
#
#
#
# lada_baklagan = Car('Lada', 'baklagan', 2015, 'baklagan', 65000, True, 145 )
#
# lada_baklagan.run_engine()
# lada_baklagan.set_increase_speed(40)
# lada_baklagan.set_decrease_speed(10)
# lada_baklagan.repainting('Blue')
# lada_baklagan.get_speed()
#
# print(lada_baklagan)

#2

# class Application:
#
#     name: list[str]
#     memory_size: float
#
#
#
#     def __init__(self, name: list[str], memory_size: float):
#
#         self.name = name
#         self.memory_size = memory_size
#
#
#
#
# class Smartahone:
#
#     brand: str
#     model: str
#     system: str
#     memory_hard: float
#     memory_fast: float
#     battery_level: float
#     is_included: bool
#     application: Application
#
#
#     def __init__(self, brand: str, model: str, system: str, memory_hard: float, memory_fast: float, battery_level: float, is_included: bool, application: Application):
#
#         self.brand = brand
#         self.model = model
#         self.system = system
#         self.memory_hard = memory_hard
#         self.memory_fast = memory_fast
#         self.battery_level = battery_level
#         self.is_included = is_included
#         self.application = application
#
#
#
#     def __str__(self):
#         return f"Brand: {self.brand}\nModel: {self.model}\nSystem: {self.system}\nBuilt-in memory: {self.memory_hard}\nRAM: {self.memory_fast}\nLevel battery: {self.battery_level}\nStatus phone: {self.is_included}\nApplication: {self.application.name}"
#
#
#     def on_phone(self):
#         self.is_included == True
#
#     def off_phone(self):
#         self.is_included == False
#
#     def set_new_system(self, new_system: str):
#
#         if new_system.lower() != self.system.lower() or new_system.lower() == '':
#             return None
#
#         self.system = new_system
#
#
#
#     def set_new_application(self, new_application: str):
#
#
#         if new_application.lower() == '':
#             return None
#
#         for item in self.application.name:
#             if item.lower() == new_application.lower():
#                 return None
#
#         self.application.name.append(new_application)
#
#
#
#
#     def delete_application(self, dell_application: str):
#
#         if dell_application.lower() == '':
#             return None
#
#
#
#         if dell_application.lower() not in self.application.name:
#             return None
#
#         target_application = None
#
#         for item in self.application.name:
#             if item.lower() == dell_application.lower():
#                 target_application = item
#                 break
#
#         self.application.name.remove(target_application)
#
#
#
#     def changer_battery(self, new_battery: float):
#
#         if new_battery == 0 or new_battery > 100 or new_battery ==  self.battery_level:
#             return None
#
#         self.battery_level == new_battery
#
#
#
#     def get_phone_is_included(self) -> bool:
#         return True if self.is_included else False
#
#     def get_level_battery(self):
#         return self.battery_level
#
#
# application = Application(['Головоломка'], 102)
#
# phone = Smartahone('Elka-Palrf', 'Razrydamet', 'RusOperationSystem_New_super_Ultra', 16, 4, 15, False, application)
#
#
#
# print(phone)

#3

class Ingredients:

    ingredients: list[str]


    def __init__(self, ingredients: list[str]):
        self.ingredients = ingredients


class Potion:

    name: str
    ingredients: Ingredients
    difficultu_preparation: int
    effect: str
    ready: bool


    def __init__(self, name: str, ingredients:Ingredients, difficultu_preparation: int, effect: str, ready: bool):
        self.name = name
        self.ingredients = ingredients
        self.difficultu_preparation = difficultu_preparation
        self.effect = effect
        self.ready = ready



    def __str__(self):
        return f'Name: {self.name}\nIngredients: { self.ingredients.ingredients}\nDifficultu preparation: {self.difficultu_preparation}\nEffect: {self.effect}\nReady: {self.ready}'





    




















































