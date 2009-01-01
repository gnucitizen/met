#    Google
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

__version__ = '1.1'
__author__ = 'Petko D. Petkov; pdp (architect)'

__doc__ = """
Google (GNUCITIZEN) pdp@gnucitizen.org
"""

import re
import http

class Sets(http.HTTPClient):
	"""
	Google Sets
	"""

	def search(self, *terms):
		"""
		search(term1, term2, term3, ...) -> []

		Extract set from terms.
		"""

		url = 'http://labs.google.com/sets?'
		_query = http.encode_url(
			[('q' + str(index + 1), value)
			 for index, value in enumerate(terms)])

		content = self.open_url(url + _query).read()

		return re.findall('<center>(.*?)\s*</center></a>', content)

class Suggest(http.HTTPClient):
	"""
	Google Suggest
	"""

	def search(self, query):
		"""
		search(query) -> []

		Suggest queries based on query.
		"""

		url = 'http://www.google.com/complete/search?'
		_query = http.encode_url({'qu': query})

		content = self.open_url(url + _query).read()
		terms = re.findall('"(.*?)",?', content)

		print terms
		return terms[3: -((len(terms) - 3)/2 + 1)]

class Cache(http.HTTPClient):
	"""
	Google Cache
	"""

	def search(self, url):
		"""
		search(url) -> string

		Get cached version of page if available.
		"""

		_url = 'http://www.google.com/search?'
		query = 'q=cache:' + urllib.quote_plus(url)

		content = self.open_url(_url + query).read()

		try: index = content.index('<hr>')
		except: raise RuntimeError('unable to get cache')

		return content[index + 5:]

class Translate(http.HTTPClient):
	"""
	Google Traslate
	"""

	def translate_text(self, text, from_lang = 'en', to_lang = 'de'):
		"""
		translate_text(text, from_lang = 'en' , to_lang = 'de') -> string

		Translate text from_lang to_lang.
		"""

		url = 'http://translate.google.com/translate_t?'
		query = http.encode_url({'langpair':from_lang + '|' + to_lang, 'text':text})

		content = self.open_url(url + query).read()
		textareas = re.findall('<textarea .*?>(.*?)</textarea>', content)

		return textareas[0].strip()

	def translate_url(self, url, from_lang = 'en', to_lang = 'de'):
		"""
		translate_url(url, from_lang = 'en', to_lang = 'de') -> string

		Traslate url from_lang to_lang.
		"""

		_url = 'http://66.249.93.104/translate_c?'
		query = http.encode_url({'langpair':from_lang + '|' + to_lang, 'u':url})

		return self.open_url(_url + query).read()

class WebSearch(http.HTTPClient):
	"""
	Google Web Search
	"""

	def search(self, query, start = 0, count = 10, filter = True):
		"""
		search(query, start = 0, count = 10, filter = True) -> results

		Search the web with Google.
		"""

		if filter: _filter = 1
		else: _filter = 0

		url = 'http://www.google.com/xhtml?'
		_query = http.encode_url({'q':query, 'start':start, 'num':count, 'filter': _filter})

		content = self.open_url(url + _query).read()

		results = []

		for item in re.findall(
			'<a href="(.*?)" accesskey="\d+">(.*?)</a>(.*?)<span class="url">',
			content):
			title = item[1]
			excerpt = item[2]
			url = item[0][item[0].index(';u=') + 3:]

			if not url.startswith('https://') and not url.startswith('ftp://'):
				url = 'http://' + url

			results.append((url, title, excerpt))

		return results

class WebCrawl(WebSearch):
	"""
	Google Search Crawl
	"""

	def crawl(self, query, count = 100):
		"""
		Craws Google's Web Search result set.

		crawl(query, count = 100) -> results
		"""

		index = 1
		last_results = None

		while True:
			if index == 1: start = 0
			else: start = (index - 1) * 100

			results = self.search(self, query, start, count)

			if last_results == results:
				break

			last_results = results

			yield results

			index = index + 1
