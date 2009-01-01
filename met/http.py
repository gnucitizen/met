#    Http
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

__version__ = '0.3'
__author__ = 'Petko D. Petkov; pdp (architect)'

__doc__ = """
Http (GNUCITIZEN) pdp@gnucitizen.org
"""

import urllib
import urllib2

def encode_url(dict):
	"""
	encode_url(dict) -> string

	Encode a dictionary into a URL query string.
	"""

	return urllib.urlencode(dict)

def decode_url(string):
	"""
	decode_url(string) -> dict

	Decode a URL query string into a dictionary.
	"""

def open_url(url, headers = {}, data = None):
	"""
	open_url(url, headers = {}, data = None) -> result

	Open url, handle errors and return the result.
	"""

	try:
		request = urllib2.Request(url, data, headers)
		result = urllib2.urlopen(request)

		if hasattr(result, 'code'):
			if result.code != 200:
				raise

	except: raise RuntimeError('request failed')
	return result

class HTTPClient(object):
	"""
	HTTPClient

	The HTTPClient object mimics standard browsers.
	"""

	def __init__(self):
		self.headers = {'User-Agent': 'Mozilla/X Gecko/X Firefox/X GNUCITIZEN/MET'}

	def open_url(self, url, headers = {}, data = None):
		"""
		open_url(url, headers = {}, data = None) -> result

		Open url, handle errors and return the result.
		"""

		_headers = {}
		_headers.update(self.headers)
		_headers.update(headers)

		return open_url(url, _headers, data)
