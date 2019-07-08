import asyncio
import time
import socket as sk

class Socket():
	def __init__(self, host, port, buffer=4069, timeout=15):
		self.s = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
		self.s.bind((host, port))

		self.buffer = buffer
		self.timeout = timeout

	async def send(self, data, target):
		self.s.sendto(data, target)

	async def recv(self, buffer=None):
		if buffer is None:
			buffer = self.buffer

		return self.s.recvfrom(buffer)

	def close(self):
		self.s.close()

	async def ping(self, target):
		start = time.time()
		self.s.sendto(b'ping', target)

		ack_time = self.await_ping_ack(self, target)

		rrt = ack_time - start

		self.s.sendto(b'rrt: ', target)

		return rrt

	def await_ping_ack(self, target):
		pass
		