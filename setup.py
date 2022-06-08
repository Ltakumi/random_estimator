from setuptools import setup

setup(
   name='random_estimator',
   version='1.0',
   description='A useful module',
   author='Man Foo',
   author_email='foomail@foo.com',
   packages=['random_estimator'],  #same as name
   install_requires=['scikit-learn', 'bar', 'greek'], #external packages as dependencies
)
