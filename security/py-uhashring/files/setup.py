# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='uhashring',
    version='%%PORTVERSION%%',
    description='Full featured consistent hashing python library compatible with ketama.',
    long_description='*********\nuhashring\n*********\n|version| |ci|\n\n.. |version| image:: https://img.shields.io/pypi/v/uhashring.svg\n.. |ci| image:: https://github.com/ultrabug/uhashring/actions/workflows/ci.yml/badge.svg\n\n**uhashring** implements **consistent hashing** in pure Python.\n\nConsistent hashing is mostly used on distributed systems/caches/databases as this avoid the total reshuffling of your key-node mappings when adding or removing a node in your ring (called continuum on libketama). More information and details about this can be found in the *literature* section.\n\nThis full featured implementation offers:\n\n- a lot of **convenient methods** to use your consistent hash ring in real world applications.\n- simple **integration** with other libs such as memcache through monkey patching.\n- a full `ketama <https://github.com/RJ/ketama>`_ compatibility if you need to use it (see important mention below).\n- all the missing functions in the libketama C python binding (which is not even available on pypi) for ketama users.\n- possibility to **use your own weight and hash functions** if you don\'t care about the ketama compatibility.\n- **instance-oriented usage** so you can use your consistent hash ring object directly in your code (see advanced usage).\n- native **pypy support**, since this is a pure python library.\n- tests of implementation, key distribution and ketama compatibility.\n\nPer node weight is also supported and will affect the nodes distribution on the ring.\n\nPython 2 EOL\n============\n\nIf you need Python 2 support, make sure to use **uhashring==1.2** as v1.2 is the last release that will support it.\n\nIMPORTANT\n=========\n\nSince v1.0 **uhashring** default has changed to use a md5 hash function with 160 vnodes (points) per node in the ring.\n\nThis change was motivated by the fact that the ketama hash function has more chances of collisions and thus requires a complete ring regeneration when the nodes topology change. This could lead to degraded performances on rapidly changing or unstable environments where nodes keep going down and up. The md5 implementation provides a linear performance when adding or removing a node from the ring!\n\nReminder: when using **uhashring** with the ketama implementation and get 40 vnodes and 4 replicas = 160 points per node in the ring.\n\nUsage\n=====\nBasic usage\n-----------\n**uhashring** is very simple and efficient to use:\n\n.. code-block:: python\n\n    from uhashring import HashRing\n\n    # create a consistent hash ring of 3 nodes of weight 1\n    hr = HashRing(nodes=[\'node1\', \'node2\', \'node3\'])\n\n    # get the node name for the \'coconut\' key\n    target_node = hr.get_node(\'coconut\')\n\nKetama usage\n------------\nSimply set the **hash_fn** parameter to **ketama**:\n\n.. code-block:: python\n\n    from uhashring import HashRing\n\n    # create a consistent hash ring of 3 nodes of weight 1\n    hr = HashRing(nodes=[\'node1\', \'node2\', \'node3\'], hash_fn=\'ketama\')\n\n    # get the node name for the \'coconut\' key\n    target_node = hr.get_node(\'coconut\')\n\nAdvanced usage\n--------------\n\n.. code-block:: python\n\n    from uhashring import HashRing\n\n    # Mapping of dict configs\n    # Ommited config keys will get a default value, so\n    # you only need to worry about the ones you need\n    nodes = {\n        \'node1\': {\n                \'hostname\': \'node1.fqdn\',\n                \'instance\': redis.StrictRedis(host=\'node1.fqdn\'),\n                \'port\': 6379,\n                \'vnodes\': 40,\n                \'weight\': 1\n            },\n        \'node2\': {\n                \'hostname\': \'node2.fqdn\',\n                \'instance\': redis.StrictRedis(host=\'node2.fqdn\'),\n                \'port\': 6379,\n                \'vnodes\': 40\n            },\n        \'node3\': {\n                \'hostname\': \'node3.fqdn\',\n                \'instance\': redis.StrictRedis(host=\'node3.fqdn\'),\n                \'port\': 6379\n            }\n        }\n\n    # create a new consistent hash ring with the nodes\n    hr = HashRing(nodes)\n\n    # set the \'coconut\' key/value on the right host\'s redis instance\n    hr[\'coconut\'].set(\'coconut\', \'my_value\')\n\n    # get the \'coconut\' key from the right host\'s redis instance\n    hr[\'coconut\'].get(\'coconut\')\n\n    # delete the \'coconut\' key on the right host\'s redis instance\n    hr[\'coconut\'].delete(\'coconut\')\n\n    # get the node config for the \'coconut\' key\n    conf = hr.get(\'coconut\')\n\nDefault node configuration\n--------------------------\n**uhashring** offers advanced node configuration for real applications, this is the default you get for every added node:\n\n.. code-block:: python\n\n    {\n        \'hostname\': nodename,\n        \'instance\': None,\n        \'port\': None,\n        \'vnodes\': 40,\n        \'weight\': 1\n    }\n\nAdding / removing nodes\n-----------------------\nYou can add and remove nodes from your consistent hash ring at any time.\n\n.. code-block:: python\n\n    from uhashring import HashRing\n\n    # this is a 3 nodes consistent hash ring\n    hr = HashRing(nodes=[\'node1\', \'node2\', \'node3\'])\n\n    # this becomes a 2 nodes consistent hash ring\n    hr.remove_node(\'node2\')\n\n    # add back node2\n    hr.add_node(\'node2\')\n\n    # add node4 with a weight of 10\n    hr.add_node(\'node4\', {\'weight\': 10})\n\nCustomizable node weight calculation\n------------------------------------\n\n.. code-block:: python\n\n    from uhashring import HashRing\n\n    def weight_fn(**conf):\n        """Returns the last digit of the node name as its weight.\n\n        :param conf: node configuration in the ring, example:\n            {\n             \'hostname\': \'node3\',\n             \'instance\': None,\n             \'nodename\': \'node3\',\n             \'port\': None,\n             \'vnodes\': 40,\n             \'weight\': 1\n            }\n        """\n        return int(conf[\'nodename\'][-1])\n\n    # this is a 3 nodes consistent hash ring with user defined weight function\n    hr = HashRing(nodes=[\'node1\', \'node2\', \'node3\'], weight_fn=weight_fn)\n\n    # distribution with custom weight assignment\n    print(hr.distribution)\n\n    # >>> Counter({\'node3\': 240, \'node2\': 160, \'node1\': 80})\n\nCustomizable hash function\n--------------------------\n\n.. code-block:: python\n\n    from uhashring import HashRing\n\n    # import your own hash function (must be a callable)\n    # in this example, MurmurHash v3\n    from mmh3 import hash as m3h\n\n    # this is a 3 nodes consistent hash ring with user defined hash function\n    hr = HashRing(nodes=[\'node1\', \'node2\', \'node3\'], hash_fn=m3h)\n\n    # now all lookup operations will use the m3h hash function\n    print(hr.get_node(\'my key hashed by your function\'))\n\nHashRing options\n----------------\n- **nodes**: nodes used to create the continuum (see doc for format).\n- **hash_fn**: use this callable function to hash keys, can be set to \'ketama\' to use the ketama compatible implementation.\n- **vnodes**: default number of vnodes per node.\n- **weight_fn**: user provided function to calculate the node\'s weight, gets the node conf dict as kwargs.\n- **replicas**: use this to change ketama ring replicas (default: 4)\n\nAvailable methods\n-----------------\n- **add_node(nodename, conf)**: add (or overwrite) the node in the ring with the given config.\n- **get(key)**: returns the node object dict matching the hashed key.\n- **get_key(key)**: alias of the current hashi method, returns the hash of the given key.\n- **get_instances()**: returns a list of the instances of all the configured nodes.\n- **get_node(key)**: returns the node name of the node matching the hashed key.\n- **get_node_hostname(key)**: returns the hostname of the node matching the hashed key.\n- **get_node_instance(key)**: returns the instance of the node matching the hashed key.\n- **get_node_port(key)**: returns the port of the node matching the hashed key.\n- **get_node_pos(key)**: returns the index position of the node matching the hashed key.\n- **get_node_weight(key)**: returns the weight of the node matching the hashed key.\n- **get_nodes()**: returns a list of the names of all the configured nodes.\n- **get_points()**: returns a ketama compatible list of (position, nodename) tuples.\n- **get_server(key)**: returns a ketama compatible (position, nodename) tuple.\n- **hashi(key)**: returns the hash of the given key (on ketama mode, this is the same as libketama).\n- **iterate_nodes(key, distinct)**: hash_ring compatibility implementation, same as range but returns tuples as a generator.\n- **print_continuum()**: prints a ketama compatible continuum report.\n- **range(key, size, unique)**: returns a (unique) list of max (size) nodes\' configuration available in the consistent hash ring.\n- **regenerate**: regenerate the ring from the current nodes configuration, useful only when using *weight_fn*.\n- **remove_node(nodename)**: remove the given node from the ring\n\nAvailable properties\n--------------------\n- **conf**: dict of all the nodes and their configuration.\n- **continuum**: same as ring.\n- **distribution**: counter of the nodes distribution in the consistent hash ring.\n- **nodes**: same as conf.\n- **ring**: hash key/node mapping of the consistent hash ring.\n- **size**: size of the consistent hash ring.\n\nIntegration (monkey patching)\n=============================\nYou can benefit from a consistent hash ring using **uhashring** monkey patching on the following libraries:\n\npython-memcached\n----------------\n\n.. code-block:: python\n\n    import memcache\n\n    from uhashring import monkey\n    monkey.patch_memcache()\n\n    mc = memcache.Client([\'node1:11211\', \'node2:11211\'])\n\nInstallation\n============\nPypi\n----\nUsing pip:\n\n.. code-block:: sh\n\n    $ pip install uhashring\n\nGentoo Linux\n------------\nUsing emerge:\n\n.. code-block:: sh\n\n    $ sudo emerge -a uhashring\n\nBenchmark\n=========\nUsage of the ketama compatible hash (default) has some performance impacts.\nContributions are welcome as to ways of improving this !\n\n    There is a big performance gap in the hash calculation between\n    the ketama C binding and its pure python counterpart.\n\n    Python 3 is doing way better than python 2 thanks to its\n    native bytes/int representation.\n\n    Quick benchmark, for 1 million generated ketama compatible keys:\n        - python_ketama C binding: 0.8427069187164307 s\n        - python 2: 5.462762832641602 s\n        - python 3: 3.570068597793579 s\n        - pypy: 1.6146340370178223 s\n\n    When using python 2 and ketama compatibility is not important, you\n    can get a better hashing speed using the other provided hashing.\n\n    hr = HashRing(nodes=[], compat=False)\n\n    Quick benchmark, for 1 million generated hash keys:\n        - python 2: 3.7595579624176025 s\n        - python 3: 3.268343687057495 s\n        - pypy: 1.9193649291992188 s\n\nLiterature\n==========\n- consistent hashing: https://en.wikipedia.org/wiki/Consistent_hashing\n- web caching paper: http://www8.org/w8-papers/2a-webserver/caching/paper2.html\n- research paper: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.23.3738\n- distributed hash table: https://en.wikipedia.org/wiki/Distributed_hash_table\n\nLicense\n=======\nBSD\n',
    author_email='Ultrabug <ultrabug@ultrabug.net>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=[
        'uhashring',
    ],
)