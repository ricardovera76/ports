#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['asdf',
 'asdf.commands',
 'asdf.commands.tests',
 'asdf.commands.tests.data',
 'asdf.compat',
 'asdf.extension',
 'asdf.extern',
 'asdf.tags',
 'asdf.tags.core',
 'asdf.tags.core.tests',
 'asdf.tags.core.tests.data',
 'asdf.testing',
 'asdf.tests',
 'asdf.tests.data']

package_data = \
{'': ['*']}

install_requires = \
['asdf-standard >=1.0.1',
 'asdf-transform-schemas >=0.2.2',
 'jmespath >=0.6.2',
 'jsonschema >=4.0.1, <4.10.0',
 'numpy >=1.10',
 'packaging >=16.0',
 'pyyaml >=3.10',
 'semantic_version >=2.8']

extras_require = \
{':python_version <"3.9"': ['importlib_resources >=3'],
 'all': ['lz4 >=0.10'],
 'docs': ['sphinx-asdf >=0.1.4'],
 'tests': ['astropy >=5.0.4',
           'gwcs',
           'pytest-doctestplus',
           'pytest-remotedata',
           'pytest-openfiles',
           'psutil',
           'lz4 >=0.10'],
 'tests:sys_platform !="win32"': ['pytest >=6.0.0'],
 'tests:sys_platform =="win32"': ['pytest !=7.1.0, !=7.1.1, !=7.1.2']}

entry_points = \
{'onsole_scripts': ['asdftool = asdf.commands.main:main'],
 'asdf_extensions': ['builtin = asdf.extension:BuiltinExtension'],
 'asdf.resource_mappings': ['asdf = asdf.resource:get_json_schema_resource_mappings'],
 'pytest11': ['asdf_schema_tester = pytest_asdf.plugin']}

setup(name='asdf',
      version='%%PORTVERSION%%',
      description='Python implementation of the ASDF Standard',
      author=None,
      author_email='The ASDF Developers <help@stsci.edu>',
      url=None,
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      extras_require=extras_require,
      entry_points=entry_points,
      python_requires='>=3.8',
     )