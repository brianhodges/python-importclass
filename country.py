class Country:
	
	def __init__(self, arg1, arg2, arg3, arg4):
		self.name = arg1
		self.population = arg2
		self.states = arg3
		self.best_city = arg4
		
	def fav_cnt(self):
		return len(self.states)

class City:
	
	def __init__(self, arg1, arg2):
		self.name = arg1
		self.population = arg2
