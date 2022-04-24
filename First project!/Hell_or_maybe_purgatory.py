class prisoners:
		
	def __init__(self, name, time, reason, is_on_death):
		self.name = name
		self.time = time
		self.reason = reason
		self.is_on_death = is_on_death
	def on_bail(self):
		if self.time <= 100:
			return True
		else:
			return False

class question:
	def __init__(self, prompt, answer):
		self.prompt = prompt
		self.answer = answer

class jailer:
	def __init__(self, tame, riot):
		self.tame = tame
		self.riot = riot





