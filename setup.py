from setuptools import setup

setup(
    name='ruben-flask-helloworld',
    version='0.1.0',
    long_description=__doc__,
    packages=['ruben_helloworld'],
    package_data = {
        'ruben_helloworld': ['share/*', 'static/*', '/templates/*'],
    },
    zip_safe=False,
    install_requires=['Flask']
)
