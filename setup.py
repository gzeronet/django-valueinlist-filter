from setuptools import setup, find_packages

setup(
    name='django-valueinlist-filter',
    version='0.1',
    description='Queryset can be filtered by a given list on the django admin page, just like: qs.filter(field__in=[list])',
    long_description=open('README.md').read(-1),
    author='Chris Chen',
    author_email='gzerone@gmail.com',
    url='http://github.com/gzeronet/django-valueinlist-filter',
    keywords=[
        'django admin',
        'django filter query',
        'django value in list',
    ],
    install_requires=[
        'Django>=1.5',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    license = 'BSD',
)
