#    Whois
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
Whois (GNUCITIZEN) pdp@gnucitizen.org
"""

import socket

class Client(object):
	"""
	Client
	"""

	def __init__(self, host, port = 43):
		self.socket = socket.TCPSocket(host, port)

	def query(self, query):
		"""
		query(query) -> result

		Perform whois query.
		"""

		try:
			self.socket.send(query)
			result = self.socket.recv()

		except: raise RuntimeError('request failed')
		return result
