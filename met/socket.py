#    Socket
#    Copyright (C) 2005-2007  Petko D. Petkov (GNUCITIZEN) pdp@gnucitizen.org
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

__version__ = '0.1'
__author__ = 'Petko D. Petkov; pdp (architect)'

__doc__ = """
Socket (GNUCITIZEN) pdp@gnucitizen.org
"""

import utils
module_name, socket = utils.python_import('socket')

class TCPSocket(object):
	"""
	TCPSocket
	"""

	def __init__(self, host, port):
		self.host = host
		self.port = port

		try:
			self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.socket.connect((host, port))

		except: raise RuntimeError('unable to connect')

	def send(self, data):
		"""
		send(data) -> None

		Send data through socket.
		"""

		try: self.socket.sendall(data)
		except: raise RuntimeError('unable to send')

	def recv(self, amount = 0):
		"""
		recv(self, amount = 0) -> data

		Recv data through socket.
		"""

		data = ''

		try:
			while True:
				_data = self.socket.recv(8192)

				if not _data:
					break

				data += _data

		except: raise RuntimeError('unable to recv')

		return data
