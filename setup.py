from setuptools import setup, find_packages
from distutils.util import convert_path

with open('README.md', 'r') as fh:
    long_description = fh.read()

main_ns = {}
ver_path = convert_path('cuba_weather/weather.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

setup(
    name='cuba_weather',
    version=main_ns['__version__'],
    packages=find_packages(),
    entry_points={'console_scripts': ['cuba-weather=cuba_weather.weather:main'],},
    url='https://github.com/daxslab/cuba-weather',
    license='MIT',
    author='Cuban Open Source Community',
    description='Python3 client for (https://www.redcuba.cu) weather API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'python-Levenshtein==0.12.0',
    ],
    python_requires='>=3.6',
)
