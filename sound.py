import asyncio
import pyaudio

from zlib import compress, decompress

class SoundInterface():
	p = pyaudio.PyAudio()

	def __init__(self, input=False, output=False, width=2, channels=2, rate=44100, buffer=1024, input_device=None, output_device=None):

		self.stream = SoundInterface.p.open(
			format=SoundInterface.p.get_format_from_width(width),
			channels=channels,
			rate=rate,
			input=input,
			output=output,
			frames_per_buffer=buffer,
			input_device_index=input_device,
			output_device_index=output_device,
		)

		self.buffer = buffer


	def write(self, data, buffer=None):
		'''Sends audio to output'''

		if buffer is None:
			buffer = self.buffer

		data = decompress(data)

		self.stream.write(data, buffer)

	@asyncio.coroutine
	def read(self, buffer=None):
		'''Returns what was listened on microphone'''
		if buffer is None:
			buffer = self.buffer

		while True:
			try:
				yield compress(self.stream.read(buffer))
			except OSError as e:
				#Does it works on other platforms (linux/osx)?
				if e.errno == -9988:
					return

	def close(self):
		self.stream.stop_stream()
		self.stream.close()

	def terminate(self):
		SoundInterface.p.terminate()

async def main():
	chunk = 1024
	rate = 44100
	record = 5

	# for e in range(SoundInterface.p.get_device_count()):
	# 	print(SoundInterface.p.get_device_info_by_index(e))

	mic = SoundInterface(input=True, input_device=0)
	sound = SoundInterface(output=True)

	h = 0
	for data in mic.read():
		h += 1
		sound.write(data)
		if h > 200:
			mic.close()

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())

