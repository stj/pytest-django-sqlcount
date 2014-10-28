import setuptools

setuptools.setup(name='pytest-django-sqlcount',
                 version='0.1.0',
                 description='py.test plugin for reporting the number of SQLs '
                             'executed per django testcase.',
                 long_description=open('README.rst').read().strip(),
                 author='Stefan Tjarks',
                 author_email='stefan [at] tjarks [dot] de',
                 url='https://github.com/stj/pytest-django-sqlcount',
                 py_modules=['pytest_django_sqlcount'],
                 install_requires=['py>=1.4.22',
                                   'pytest>=2.6.0',
                                   'pytest-django>=2.7.0'],
                 entry_points={'pytest11': [
                     'django_sqlcount = pytest_django_sqlcount',
                     ]
                 },
                 license='MIT License',
                 zip_safe=False,
                 keywords='py.test pytest django sqlcount',
                 classifiers=['Development Status :: 4 - Beta',
                              'Intended Audience :: Developers',
                              'License :: OSI Approved :: MIT License',
                              'Operating System :: OS Independent',
                              'Programming Language :: Python',
                              'Programming Language :: Python :: 2.7',
                              'Topic :: Software Development :: Testing'])
