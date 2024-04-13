from appliances.kitchen.utility import DishWasher
from appliances.laundry import Dryer
from appliances.laundry import Washer
from appliances.kitchen.utility import Refrigerator
from appliances.kitchen import CoffeeMaker
from appliances.appliance import Appliance
from appliances.kitchen import CanOpener

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red", "normal")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

tin_pin = CanOpener("silver")
tin_pin.open_can()
