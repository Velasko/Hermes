from . import settings

class User():
	def __init__(self, username, address, server=None, volume=1, comm_device=None):
		self.username = username
		self.address = address

		self.volume = volume

		self.comm_device = comm_device
		if comm_device is None:
			self.comm_device = settings.default_comm

		self.server = server
		if server is None:
			self.server = self

	def __eq__(self, other):
		if isinstance(other, User):
			return self.address == other.address
		return False