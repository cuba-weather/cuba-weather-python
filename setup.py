from setuptools import setup

from cuba_weather.console import __version__

setup(
    name='cuba_weather',
    version=__version__,
    packages=['cuba_weather'],
    entry_points={'console_scripts': ['cuba-weather=cuba_weather.console:main'],},
    url='https://github.com/daxslab/cuba-weather',
    license='MIT',
    author='Cuban Open Source Community',
    description='Python3 client for (https://www.redcuba.cu) weather API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
