#    Netcraft
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

__version__ = '1.0'
__author__ = 'Petko D. Petkov; pdp (architect)'

__doc__ = """
Netcraft (GNUCITIZEN) pdp@gnucitizen.org
"""

import re
import http

class Netcraft(http.HTTPClient):
	"""
	Netcraft

	Netcraft wrapper.
	"""

	def query_dns(self, query, last = '', page = 0):
		"""
		query_dns(query, last = '', page = 0) -> results

		Query the dns database of netcraft.
		"""

		type = 'site contains'
		tokens = query.split(':')

		if len(tokens) != 1:
			if tokens[0] == 'contains': type = 'site contains'
			elif tokens[0] == 'starts': type = 'site starts with'
			elif tokens[0] == 'ends': type = 'site ends with'
			elif tokens[0] == 'subdomain': type = 'subdomain matches'

			host = tokens[1]

		else:
			host = tokens[0]

		url = 'http://searchdns.netcraft.com/?'
		_query = http.encode_url(
			{'host':host,
			 'last':last,
			 'from':(page * 20) + 1,
			 'restriction':type})

		content = self.open_url(url + _query).read()

		results = []

		for item in re.findall(
			'<td align="left">\n' +
			'<a href="(.*?)">.*?</a></td>\n' +
			'<td align="center">.*?</td>\n' +
			'<td>(.*?)</td>\n' +
			'<td><a href=".*?q=(.*?)">(.*?)</a></td>\n' + 
			'<td><a href=".*?">(.*?)</a></td>',
			content): results.append((
				re.match('.*?://(.*?)/', item[0]).group(1),
				item[1],
				item[3],
				item[2],
				item[4]))

		return results

class NetcraftCrawl(Netcraft):
	"""
	Netcraft

	Netcraft Crawler
	"""

	def crawl_dns(self, query, level = 0):
		"""
		crawl_dns(query, level = 0) -> generator

		Crawl the dns database of netcraft.
		"""

		last = ''
		page = 0
		last_results = {}

		while True:
			try:
				results = self.query_dns(query, last, page)

				if not results or results == last_results:
					raise

			except:
				break

			yield results

			last = results[-1][0]
			page += 1
			last_results = results
