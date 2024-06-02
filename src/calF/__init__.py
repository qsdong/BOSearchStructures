
from os.path import dirname, basename, isfile, join
import glob
modules = glob.glob(join(dirname(__file__),"*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
for _ in __all__:
    exec(f"from .{_} import *")
# print(__all__)