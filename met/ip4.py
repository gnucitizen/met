#    IP4
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
IP4 (GNUCITIZEN) pdp@gnucitizen.org
"""

def ip_to_unsigned_int(ip):
	"""
	ip_to_unsigned_int(ip) -> unsigned int

	Convert ip address to unsigned int.
	"""

	tokens = ip.split('.')

	return 16777216 * int(tokens[0]) + \
	       65536 * int(tokens[1]) + \
	       256 * int(tokens[2]) + \
	       int(tokens[3])

def unsigned_int_to_ip(unsigned_int):
	"""
	unsigned_int_to_ip(number) -> ip

	Convert unsigned int to ip.
	"""

	return '%d.%d.%d.%d' % \
	       (unsigned_int/16777216%256,
	        unsigned_int/65536%256,
	        unsigned_int/256%256,
	        unsigned_int%256)

def cidr_to_range(cidr):
	"""
	cidr_to_range() -> (network address, broadcast address)

	Convert cidr to range
	"""

	tokens = cidr.split('/')

	start = ip_to_unsigned_int(tokens[0])
	stop = pow(2, 32 - int(tokens[1])) + start - 1

	return (start, stop)
