import glob
import distutils.core

data_files = [
	('etc/met/', glob.glob('etc/*')),
	('doc/met/', ['COPYING', 'README'])]

distutils.core.setup(
	version      = '1.0b',
	description  = 'Massive Enumeration Toolset (MET)',
	author       = 'Petko D. Petkov; pdp (architect)',
	author_email = 'pdp@gnucitizen.org',
	url          = 'http://www.gnucitizen.org/projects/met',
	packages     = ['met'],

	scripts      = glob.glob('scripts/*'),
	data_files   = data_files)
