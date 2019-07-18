from .sound import SoundInterface
from .connection import Socket

class default_settings():
	def __init__(self):
		self.default_comm = SoundInterface(input=True, output=True)
		self.default_socket = Socket(host='127.0.0.1', port=5000)

settings = default_settings()