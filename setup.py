from distutils.core import setup

from os.path import dirname, abspath, join

curr_file_path = dirname(abspath(__file__))

setup(
    name='devut',
    version='0.0.1',
    description='dev utils to reduce copy paste',
    author='Alex Buchkovsky',
    author_email='olex.buchkovsky@gmail.com',
    url='https://github.com/ahcub/armory',
    packages=['algorithms', 'os_utils'],
    package_dir={
        'algorithms': join(curr_file_path, 'algorithms'),
        'os_utils': join(curr_file_path, 'os_utils')
    }
)
