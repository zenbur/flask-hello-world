from setuptools import setup

setup(
    name='flask-helloworld',
    version='0.1.0',
    long_description=__doc__,
    packages=['helloworld'],
    include_package_data=True,
    zip_safe=False,
    scripts=['run_helloworld.py'],
    install_requires=['Flask']
)
