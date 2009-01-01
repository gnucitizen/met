#    Shell
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

__version__ = '1.0b'
__author__ = 'Petko D. Petkov; pdp (architect)'

__doc__ = """
Shell (GNUCITIZEN) pdp@gnucitizen.org
"""

import subprocess

class Shell:
	"""
	Shell

	Spawn shell object.
	"""

	def __init__(self):
		self.env = {}

		self.stdin = None
		self.stdout = None
		self.stderr = None

		self.wait = False

	def __getitem__(self, command):
		"""
		x.__getitem__(y) <==> x[y]
		"""

		def _call(*args):
			self.__call__(command + ' ' + ' '.join(args))

		return _call

	def __getattr__(self, command):
		"""
		x.__getattribute__('name') <==> x.name
		"""

		def _call(*args):
			self.__call__(command + ' ' + ' '.join(args))

		return _call

	def __call__(self, command):
		"""
		x.__call__(...) <==> x(...)
		"""

		process = subprocess.Popen(
			args = command.split(),
			env = self.env,
			stdin = subprocess.PIPE,
			stdout = subprocess.PIPE,
			close_fds = False,
			universal_newlines = True)

		if self.wait: return_code = process.wait()
		else: return_code = process.returncode

		self.stdin = process.stdin
		self.stdout = process.stdout
		self.stderr = process.stderr

		return return_code
