import sys

import pytest
from _pytest.runner import pytest_runtest_makereport as prm
from _pytest.terminal import TerminalReporter


def pytest_addoption(parser):
    group = parser.getgroup("django")
    group._addoption(
        '--sqlcount', action="store_true", dest="sqlcount", default=False,
        help="Outputs the number of SQLs per test on default DB connection.")


@pytest.mark.trylast
def pytest_configure(config):
    if hasattr(config, 'slaveinput'):
        return
    if config.option.sqlcount:
        config._sql = SQLCountTerminalReporter(config, sys.stdout)
        standard_reporter = config.pluginmanager.getplugin('terminalreporter')
        config.pluginmanager.unregister(standard_reporter)
        config.pluginmanager.register(config._sql, 'terminalreporter')


def pytest_unconfigure(config):
    sqlcount = getattr(config, '_sql', None)
    if sqlcount:
        del config._sql
        config.pluginmanager.unregister(sqlcount)


class SQLCountTerminalReporter(TerminalReporter):
    def __init__(self, config, file=None):
        self.sqlcount = config.getvalue('sqlcount')
        if self.sqlcount and not config.option.verbose:
            config.option.verbose = 1
        TerminalReporter.__init__(self, config, file)

    def pytest_runtest_logreport(self, report):
        TerminalReporter.pytest_runtest_logreport(self, report)
        res = self.config.hook.pytest_report_teststatus(report=report)
        cat, letter, word = res
        if not letter and not word:
            # probably passed setup/teardown
            return
        if self.sqlcount:
            self._tw.write(" %d" % report.sqlcount, blue=True)


def pytest_runtest_makereport(item, call):
    report = prm(item, call)
    report.sqlcount = len(getattr(item, 'sqlcount', []))
    return report


def pytest_runtest_call(item):
    from django.db import connection
    from django.test.utils import CaptureQueriesContext

    with CaptureQueriesContext(connection) as cqc:
        item.runtest()
    item.sqlcount = cqc
