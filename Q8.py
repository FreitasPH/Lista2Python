import abc

class Client(object):
	__metaclass__ = abc.ABCMeta

	#With the abstract method we can define a method as a
	#placeholder for methods used in the heir classes
	@abc.abstractmethod
	def get_haircolor(self):
		"""Returns the clients hair color"""

class BrunetteClient(Client):
	
	haircolor = "Brown"
	
	#With clas methods we can instance classes instead of objects.
	#Useful when we dont need to access the objects
	@classmethod
	def get_haircolor(cls):
		return cls.haircolor

class BaldClient(Client):
	
	#Using static methods we dont need information about the object nor the class
	@staticmethod
	def get_haircolor():
		return "The client has no hair"

Alex = BrunetteClient()
print(Alex.get_haircolor())
John = BaldClient()
print(John.get_haircolor())


