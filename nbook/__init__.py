import sys
from . import nbook

sys.meta_path.append(nbook.NotebookFinder())
