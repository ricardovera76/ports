# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='nbconvert',
    version='%%PORTVERSION%%',
    description='Converting Jupyter Notebooks',
    long_description='# nbconvert\n\n### Jupyter Notebook Conversion\n\n[![Google Group](https://img.shields.io/badge/-Google%20Group-lightgrey.svg)](https://groups.google.com/forum/#!forum/jupyter)\n[![Build Status](https://travis-ci.org/jupyter/nbconvert.svg?branch=main)](https://travis-ci.org/jupyter/nbconvert)\n[![Documentation Status](https://readthedocs.org/projects/nbconvert/badge/?version=latest)](https://nbconvert.readthedocs.io/en/latest/?badge=latest)\n[![Documentation Status](https://readthedocs.org/projects/nbconvert/badge/?version=stable)](https://nbconvert.readthedocs.io/en/stable/?badge=stable)\n[![codecov.io](https://codecov.io/github/jupyter/nbconvert/coverage.svg?branch=main)](https://codecov.io/github/jupyter/nbconvert?branch=main)\n[![CircleCI Docs Status](https://circleci.com/gh/jupyter/nbconvert/tree/main.svg?style=svg)](https://circleci.com/gh/jupyter/nbconvert/tree/main)\n\nThe **nbconvert** tool, `jupyter nbconvert`, converts notebooks to various other\nformats via [Jinja][] templates. The nbconvert tool allows you to convert an\n`.ipynb` notebook file into various static formats including:\n\n- HTML\n- LaTeX\n- PDF\n- Reveal JS\n- Markdown (md)\n- ReStructured Text (rst)\n- executable script\n\n## Usage\n\nFrom the command line, use nbconvert to convert a Jupyter notebook (_input_) to a\na different format (_output_). The basic command structure is:\n\n    $ jupyter nbconvert --to <output format> <input notebook>\n\nwhere `<output format>` is the desired output format and `<input notebook>` is the\nfilename of the Jupyter notebook.\n\n### Example: Convert a notebook to HTML\n\nConvert Jupyter notebook file, `mynotebook.ipynb`, to HTML using:\n\n    $ jupyter nbconvert --to html mynotebook.ipynb\n\nThis command creates an HTML output file named `mynotebook.html`.\n\n## Dev Install\n\nCheck if pandoc is installed (`pandoc --version`); if needed, install:\n\n```\nsudo apt-get install pandoc\n```\n\nOr\n\n```\nbrew install pandoc\n```\n\nInstall nbconvert for development using:\n\n```\ngit clone https://github.com/jupyter/nbconvert.git\ncd nbconvert\npip install -e .\n```\n\nRunning the tests after a dev install above:\n\n```\npip install nbconvert[test]\npy.test --pyargs nbconvert\n```\n\n## Documentation\n\n- [Documentation for Jupyter nbconvert](https://nbconvert.readthedocs.io/en/latest/)\n  [[PDF](https://media.readthedocs.org/pdf/nbconvert/latest/nbconvert.pdf)]\n- [nbconvert examples on GitHub](https://github.com/jupyter/nbconvert-examples)\n- [Documentation for Project Jupyter](https://jupyter.readthedocs.io/en/latest/index.html)\n  [[PDF](https://media.readthedocs.org/pdf/jupyter/latest/jupyter.pdf)]\n\n## Technical Support\n\n- [Issues and Bug Reports](https://github.com/jupyter/nbconvert/issues): A place to report\n  bugs or regressions found for nbconvert\n- [Community Technical Support and Discussion - Discourse](https://discourse.jupyter.org/): A place for\n  installation, configuration, and troubleshooting assistannce by the Jupyter community.\n  As a non-profit project and maintainers who are primarily volunteers, we encourage you\n  to ask questions and share your knowledge on Discourse.\n\n## Jupyter Resources\n\n- [Jupyter mailing list](https://groups.google.com/forum/#!forum/jupyter)\n- [Project Jupyter website](https://jupyter.org)\n\n[jinja]: http://jinja.pocoo.org/\n',
    author_email='Jupyter Development Team <jupyter@googlegroups.com>',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'beautifulsoup4',
        'bleach',
        'defusedxml',
        'importlib-metadata>=3.6; python_version < "3.10"',
        'jinja2>=3.0',
        'jupyter-core>=4.7',
        'jupyterlab-pygments',
        'lxml',
        'markupsafe>=2.0',
        'mistune<3,>=2.0.3',
        'nbclient>=0.5.0',
        'nbformat>=5.1',
        'packaging',
        'pandocfilters>=1.4.1',
        'pygments>=2.4.1',
        'tinycss2',
        'traitlets>=5.0',
    ],
    extras_require={
        'all': [
            'ipykernel',
            'ipython',
            'ipywidgets>=7',
            'nbsphinx>=0.2.12',
            'pre-commit',
            'pyppeteer<1.1,>=1',
            'pyqtwebengine>=5.15',
            'pytest',
            'pytest-cov',
            'pytest-dependency',
            'sphinx-rtd-theme',
            'sphinx==5.0.2',
            'tornado>=6.1',
        ],
        'docs': [
            'ipython',
            'nbsphinx>=0.2.12',
            'sphinx-rtd-theme',
            'sphinx==5.0.2',
        ],
        'qtpdf': [
            'pyqtwebengine>=5.15',
        ],
        'qtpng': [
            'pyqtwebengine>=5.15',
        ],
        'serve': [
            'tornado>=6.1',
        ],
        'test': [
            'ipykernel',
            'ipywidgets>=7',
            'pre-commit',
            'pyppeteer<1.1,>=1',
            'pytest',
            'pytest-cov',
            'pytest-dependency',
        ],
        'webpdf': [
            'pyppeteer<1.1,>=1',
        ],
    },
    entry_points={
        'console_scripts': [
            'jupyter-dejavu = nbconvert.nbconvertapp:dejavu_main',
            'jupyter-nbconvert = nbconvert.nbconvertapp:main',
        ],
        'nbconvert.exporters': [
            'asciidoc = nbconvert.exporters:ASCIIDocExporter',
            'custom = nbconvert.exporters:TemplateExporter',
            'html = nbconvert.exporters:HTMLExporter',
            'latex = nbconvert.exporters:LatexExporter',
            'markdown = nbconvert.exporters:MarkdownExporter',
            'notebook = nbconvert.exporters:NotebookExporter',
            'pdf = nbconvert.exporters:PDFExporter',
            'python = nbconvert.exporters:PythonExporter',
            'qtpdf = nbconvert.exporters:QtPDFExporter',
            'qtpng = nbconvert.exporters:QtPNGExporter',
            'rst = nbconvert.exporters:RSTExporter',
            'script = nbconvert.exporters:ScriptExporter',
            'slides = nbconvert.exporters:SlidesExporter',
            'webpdf = nbconvert.exporters:WebPDFExporter',
        ],
    },
    packages=[
        'nbconvert',
        'nbconvert.exporters',
        'nbconvert.exporters.tests',
        'nbconvert.filters',
        'nbconvert.filters.tests',
        'nbconvert.postprocessors',
        'nbconvert.postprocessors.tests',
        'nbconvert.preprocessors',
        'nbconvert.preprocessors.tests',
        'nbconvert.resources',
        'nbconvert.tests',
        'nbconvert.utils',
        'nbconvert.utils.tests',
        'nbconvert.writers',
        'nbconvert.writers.tests',
    ],
)