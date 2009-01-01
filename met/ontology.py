#    Ontology
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
Ontology (GNUCITIZEN) pdp@gnucitizen.org
"""

import store

class __Literal(store.Literal):
	def __init__(self, value):
		self.prefix = self.__class__.__name__.lower()
		self.value = value

class __Predicate(store.Predicate):
	def __init__(self):
		self.value = self.__class__.__name__.lower()

class IPv4(__Literal): pass
class IPv6(__Literal): pass
class Host(__Literal): pass
class Name(__Literal): pass
class Port(__Literal): pass
class Domain(__Literal): pass

class hasIPv4(__Predicate): pass
class hasIPv6(__Predicate): pass
class hasPort(__Predicate): pass
class hasName(__Predicate): pass
class hasValue(__Predicate): pass
class hasDomain(__Predicate): pass
