#    Store
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
Store (GNUCITIZEN) pdp@gnucitizen.org
"""

class Subject(object):
	def __str__(self):
		return self.prefix + ':' + self.value

class Predicate(object):
	def __str__(self):
		return self.prefix + ':' + self.value

class Object(object):
	def __str__(self):
		return self.prefix + ':' + self.value

class Literal(object):
	def __str__(self):
		return self.prefix + ':' + self.value

class MemoryBackend(object):
	"""
	MemoryBackend() -> MemoryBackend

	Make memory backend.
	"""

	def __init__(self):
		self.triples = []

	def __matches(self, tripleA, tripleB):
		count = 0
		indexes = []

		if tripleA[0] is not None: indexes.append(0)
		if tripleA[1] is not None: indexes.append(1)
		if tripleA[2] is not None: indexes.append(2)

		for index in indexes:
			if tripleA[index] == tripleB[index]:
				count += 1

		if count == len(indexes):
			return True

		return False

	def insert(self, subject = '', predicate = '', object = ''):
		"""
		insert(subject = '', predicate = '', object = '') -> None

		Insert single triple into store.
		"""

		self.triples.append((subject, predicate, object))

	def remove(self, subject = '', predicate = '', object = ''):
		"""
		remove(subject = '', predicate = '', object = '') -> None

		Remove single triple defined by any of the above arguments.
		"""

		for triple in self.triples:
			if self.__matches((subject, predicate, object), triple):
				self.triples.remove(triple)

	def search(self, subject = '', predicate = '', object = ''):
		"""
		search(subject = '', predicate = '', object = '') -> tuple[]

		Search triples defined by any of the above arguments.
		"""

		results = []

		for triple in self.triples:
			if self.__matches((subject, predicate, object), triple):
				results.append(triple)

		return results

class Store(object):
	"""
	Store(backend = MemoryBackend()) -> Store

	Make triple store.
	"""

	def __init__(self, backend = MemoryBackend()):
		self.backend = backend

	def insert(self, subject = '', predicate = '', object = ''):
		"""
		insert(subject = '', predicate = '', object = '') -> None

		Insert single triple into store.
		"""

		return self.backend.insert(subject, predicate, object)

	def remove(self, subject = '', predicate = '', object = ''):
		"""
		remove(subject = '', predicate = '', object = '') -> None

		Remove single triple defined by any of the above arguments.
		"""

		return self.backend.remove(subject, predicate, object)

	def search(self, subject = '', predicate = '', object = ''):
		"""
		search(subject = '', predicate = '', object = '') -> tuple[]

		Search triples defined by any of the above arguments.
		"""

		return self.backend.search(subject, predicate, object)
