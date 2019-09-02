#Inheritance --> sharing properties with other classes
# OOP
# import importlib
# importlib.reload(cars)

#class Vehicle
class Vehicle:

	#Constructor
	def __init__(self,make,model, fuel="gas"):

		self.make = make
		self.model = model
		self.fuel = fuel

	def is_eco_friendly(self):
		if self.fuel == "gas":
			return False
		else:
			return True

#class Car ---> inherits properties of the Vehicle class
class Car(Vehicle):

	#Constructor
	def __init__(self,make,model,fuel="gas", num_wheels=4):

		#calling the constructor on my Vehicle class---> super() keyword is used to do so
		super().__init__(make,model,fuel)
		self.num_wheels = num_wheels
