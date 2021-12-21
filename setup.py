from setuptools import setup, find_packages
 
setup(name='odulib',
      version='0.1',
      url='https://github.com/deaflurryth/odulib',
      license='MIT',
      author='deaflurryth',
      author_email='amflurry@icloud.com',
      description='Add static script_dir() method to Path',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)