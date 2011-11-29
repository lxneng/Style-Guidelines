# -*- coding: utf-8 -*-
import sys, os

sys.path.append(os.path.abspath('_themes'))
sys.path.append(os.path.abspath('..'))


templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'Style-Guidelines'
copyright = u'2011, lxneng.com'

version = '0.1'
release = '0.1'

exclude_patterns = ['_build']

html_theme = 'flask'

html_theme_options = {
            'index_logo': 'logo.png',
            }
html_theme_path = ['_themes']

html_title = None

html_static_path = ['_static']

html_sidebars = {
    'index': ['fork-me-on-github.html', 'localtoc.html', 'searchbox.html'],
    '**': ['localtoc.html', 'relations.html', 'searchbox.html'],
}

htmlhelp_basename = 'Style-Guidelines'
