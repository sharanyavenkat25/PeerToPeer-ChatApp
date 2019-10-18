import socket
import threading
import sys

class server:
	def __init__(self):
		self.sock.bind(('0.0.0.0',10000))
		self.sock.listen(1)