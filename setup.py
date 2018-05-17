from setuptools import setup

setup(
    name='flask-helloworld',
    version='0.1.0',
    long_description=__doc__,
    packages=['helloworld'],
    package_data = {
        'helloworld': ['share/*', 'static/*', '/templates/*'],
    },
    zip_safe=False,
    install_requires=['Flask']
)
