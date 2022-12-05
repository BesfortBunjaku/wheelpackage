from setuptools import setup



setup(
    
    setup_requires=['wheel'],
    name='wheelpackage',
    version='0.0.1',
    description='A useful module',
    author='Besfort Bunjaku',
    author_email='bessffort@gmail.com',
    py_modules=['wheelpackage'],  # same as name
    # packages=['libs','scripts'],
    package_dir = {'':'src'},
    install_requires=['beautifulsoup4','requests','lxml'], # external packages as dependencies
    
  
 
)