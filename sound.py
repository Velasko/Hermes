import pyaudio

class SoundInterface():
	def __init__(self,
		input_device: int=0,
		output_device: int=0,
		buffer: int=1024,
		width: int=2,
		channels: int=2,
		rate: int=44100,
		):

		self.p = pyaudio.PyAudio()

		self.stream = self.p.open(format=p.get_format_from_width(width),
                channels=channels,
                rate=rate,
                input=True,
                output=True,
                frames_per_buffer=buffer,
                input_device_index=2)

		self.buffer = buffer

	def write(self, data, buffer=None):
		'''Sends audio to output'''

		if buffer is None:
			buffer = self.buffer

		data = self.decompress(data)

		self.stream.write(data, buffer)

	def read(self, buffer=None):
		'''Returns what was listened on microphone'''
		if buffer is None:
			buffer = self.buffer

		return self.stream.read(buffer)

	def close(self):
		self.stream.stop_stream()
		self.stream.close()

		self.p.terminate()

	def decompress(data):
		'''Inverse of compress.
		Decompresses the audio which were compressed to spare bandwidth'''
		return data

	def compress(data):
		'''Inverse of decompress.
		Compresses the audio to spare bandwidth'''
		return data