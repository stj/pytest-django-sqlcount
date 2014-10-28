pytest-django-sqlcount
======================

.. image:: https://pypip.in/download/pytest-django-sqlcount.png
    :target: https://pypi.python.org/pypi//pytest-django-sqlcount/
    :alt: Downloads

.. image:: https://pypip.in/version/pytest-django-sqlcount/.png
    :target: https://pypi.python.org/pypi/pytest-django-sqlcount/
    :alt: Latest Version

.. image:: https://pypip.in/license/pytest-django-sqlcount/.png
    :target: https://pypi.python.org/pypi/pytest-django-sqlcount/
    :alt: License

This plugin adds the number of SQLs executed on the default database connection
per test to the terminal report.

All features offered by the default py.test terminal plugin should be available.


Installation
------------

Install with pip::

    pip install pytest-django-sqlcount


Uninstallation
--------------

Uninstall with pip::

    pip uninstall pytest-django-sqlcount


Usage
-----

Running tests with SQLCount output::

    py.test --sqlcount myproj tests/


Limitation
----------

Keep in mind that test factories and fixtures can create more SQLs than the
tested method/function. SQLs created by those methods are included in the count.
