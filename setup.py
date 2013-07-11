from setuptools import setup, find_packages

setup(
    name='django-valueinlist-filter',
    version='0.1.3',
    description='Queryset can be filtered by a given list on the django admin page, just like: qs.filter(field__in=[list])',
    long_description=open('README.rst').read(-1),
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
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Environment :: Web Environment',
        'Operating System :: OS Independent'
    ],
    license='License :: OSI Approved :: BSD License',
)
