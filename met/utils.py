#    Utils
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
Utils (GNUCITIZEN) pdp@gnucitizen.org
"""

import os
import sys

def python_import(name):
	"""
	python_import(name) -> (python_module_name, python_module)

	Imports a python module based on name.
	"""

	current_path = os.path.dirname(os.path.abspath(__file__))

	base_name = os.path.basename(current_path).split('.')[0]

	sys.path[:] = [
		path for path in sys.path
		if os.path.abspath(path) != os.path.abspath(current_path)]

	original_module = sys.modules[name]

	del sys.modules[name]

	python_module = __import__(name)
	python_module_name = 'python_%s' % name

	sys.modules[python_module_name] = python_module
	sys.path.append(current_path)
	sys.modules[name] = original_module

	return python_module_name, python_module
