class Data():
	'''Translates the recieved data to an object'''
	def __init__(self, data, addr):
		self.sender = None
		self.data = None
		self.type = None #a str saying if it's ping/voice/etc
		pass

	def serialize(self):
		'''Turns wanted data into bytes to be sent over the socket'''
		pass

