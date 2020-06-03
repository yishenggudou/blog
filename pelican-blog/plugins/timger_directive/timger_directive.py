try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen
import os
import io

from docutils.parsers.rst import directives
from pelican.rstdirectives import Pygments
from matplotlib.sphinxext.plot_directive import PlotDirective
from sphinx.ext.graphviz import Graphviz


class GraphvizDirective(Graphviz):
    pass


def register():
    directives.register_directive('plot', PlotDirective)
    directives.register_directive('graphviz', GraphvizDirective)
