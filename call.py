import asyncio

from . import settings

class Call():
	def __init__(self, index=0, socket=None, mic=None, participants={}):
		self.participants = participants
		self.participants[index] = self

		self.server = None

		self.socket = socket
		if socket is None:
			self.socket = settings.default_socket

		self.mic = mic
		if mic is None:
			self.mic = settings.default_comm


	async def speak(self):

		for data in self.mic.read():
			for server in self.server
				address = server.address
				self.socket.send(data, address)
