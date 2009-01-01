#    DNS
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
DNS (GNUCITIZEN) pdp@gnucitizen.org
"""

import utils
module_name, socket = utils.python_import('socket')

def resolve(host):
    """
    resolve(host) -> []

    Resolve host.
    """

    try:
        addrinfo = socket.getaddrinfo(host, 0)

        return [info[4][0] for info in addrinfo]

    except: raise ValueError('cannot resolve %s' % host)

def reverse(host):
	"""
	reverse(host) -> []

	Reverse host.
	"""

	try:
		host, aliaslist, addr = socket.gethostbyaddr(host)

		return [host] + aliaslist

	except: raise ValueError('cannot reverse %s' % host)
