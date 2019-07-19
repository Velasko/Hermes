import socket as sk
import threading
import time

from .data import Data

class Socket():
	def __init__(self, host, port, buffer=4069, timeout=15):
		self.s = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
		self.s.bind((host, port))

		self.buffer = buffer
		self.timeout = timeout

		self.data = 1
		self.event = threading.Event()

		self.listener = threading.Thread(target=self.recv)
		self.listener.daemon = True
		self.listener.start()

	def send(self, data, target):
		self.s.sendto(data, target)

	def read(self, buffer):
		while True:
			data, addr = self.s.recvfrom(buffer)
			yield data, addr

	def wait(self):
		self.event.wait()
		return self.data

	def notify_waiters(self):
		self.event.set()
		self.event.clear()

	def recv(self, buffer=None):
		print('started reading', self.data)
		if buffer is None:
			buffer = self.buffer

		for data, addr in self.read(buffer):
			self.data = data#Data(data, addr)
			self.notify_waiters()

	def close(self):
		self.s.close()

	def ping(self, target):
		start = time.time()
		self.s.sendto(b'ping', target)

		ack_time = self.await_ping_ack(self, target)

		rrt = ack_time - start

		self.s.sendto(b'rrt: ', target)

		return rrt

	def await_ping_ack(self, target):
		while True:
			data = self.wait()
			if data.sender == target and data.type == 'ping':
				return time.time()

if __name__ == '__main__':
	print('starting connection.py')
	try:
		s = Socket(host='', port=5001)
		time.sleep(1)
		while True:
			data = s.wait()
			del data
#			print('final data:', data.decode('utf-8'))
	finally:
		s.close()