from setuptools import setup, find_packages

from serpent import __version__

setup(
    name='serpent',
    version=__version__,

    description='The Serpent',
    long_description='A facilitator of transparency and uncomfortable truths.',
    author='Arni Inaba Kjartansson',
    author_email='arni.inaba@gmail.com',
    license='BSD',

    classifiers=[
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],
    zip_safe=False,
    packages=find_packages(exclude=['tests']),
    include_package_data=True
)
