from distutils.core import setup, Extension


scws_module = Extension('pyscws',
    sources = ['scws.c', 'charset.c', 'crc32.c', 'darray.c', 'lock.c', 'pool.c',
        'rule.c', 'xdb.c', 'xdict.c', 'xtree.c']
)

setup (name = 'pyscws',
    version = '1.0',
    description = 'Python wrapped scws Segmentation Method.',
    ext_modules = [scws_module]
)

