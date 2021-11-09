import sys
import os

# We need to tell Sphinx where to look for modules
sys.path.insert(0, os.path.abspath('.'))

extensions = [
    'sphinx.ext.autodoc',  # Support automatic documentation
    'sphinx.ext.coverage', # Automatically check if functions are documented
    'sphinx.ext.mathjax',  # Allow support for algebra
    'sphinx.ext.viewcode', # Include the source code in documentation
    'numpydoc'             # Support NumPy style docstrings
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'Average Squares'
copyright = 'None'
version = '0.1'
release = '0.1'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'alabaster'
pygments_style = 'sphinx'
htmlhelp_basename = 'AverageSquaresDoc'
latex_elements = {
}

latex_documents = [
  ('index', 'Average Squares.tex', 'Average Squares Documentation',
   'MPHY0021', 'manual'),
]

man_pages = [
    ('index', 'Average Squares', 'Average Squares Documentation',
     ['MPHY0021'], 1)
]

texinfo_documents = [
  ('index', 'Average Squares', u'Average Squares Documentation',
   'MPHY0021', 'Average Squares', 'One line description of project.',
   'Miscellaneous'),
]