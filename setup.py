from setuptools import setup, find_packages
from annotator.main import __version__

requirements = [
    'docopt',
    'flask',
    'gevent',
    'numpy',
    'scikit-image',
    'opencv-python',
    'h5py',
    'pandas',
    'dataclasses',
    'av',
    'tqdm',
]

setup(
    name='annotator',
    version=__version__,
    description='GUI to manually annotate 5D images.',
    author='Vivek Venkatachalam, Mahdi Torkashvand',
    author_email='m.torkashvand@northeastern.edu',
    url='https://github.com/venkatachalamlab/annotator',
    entry_points={'console_scripts': ['annotator=annotator.main:main']},
    keywords=['manual annotation'],
    install_requires=requirements,
    packages=find_packages()
)
