import asyncio
import socket as sk

from .sound import main as sound_main

port = 5001

class test():
	def __init__(self):
		self.data = 0

	@asyncio.coroutine
	def read(self):

		try:
			s = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
			s.bind(('127.0.0.1', port))

			while True:
				self.data = s.recvfrom(1024).decode('utf-8')
				print('in read', self.data)
				yield
		finally:
			s.close()

	async def await_data(self):
		print('in await')
		for _ in self.read():
			return self.data

async def printe(test):
	print(test.data)

	await test.await_data()
	print(test.data)

async def main():
	a = test()

	loop.create_task(sound_main())
	task1 = loop.create_task(printe(a))
	task2 = loop.create_task(printe(a))

	asyncio.sleep(2)
	print('creating socket')
	s = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
	s.sendto('kek'.encode(), ('127.0.0.1', port))
	print('sent')

	asyncio.sleep(2)
	print('canceling')
	task1.cancel()
	task2.cancel()

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())