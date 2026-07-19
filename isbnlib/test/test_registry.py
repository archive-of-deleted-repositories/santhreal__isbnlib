# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file

import pytest

from ..registry import (
    add_bibformatter,
    add_service,
    bibformatters,
    services,
    setdefaultbibformatter,
    setdefaultservice,
)


# tests
def test_setdefaultbibformatter():
    """Test setdefaultbibformatter."""
    assert setdefaultbibformatter('json') == None
    with pytest.raises(Exception):
        setdefaultbibformatter('default')
    with pytest.raises(Exception):
        setdefaultbibformatter('')
    with pytest.raises(Exception):
        setdefaultbibformatter('xxx')


def test_setdefaultservice():
    """Test setdefaultservice."""
    assert setdefaultservice('goob') == None
    with pytest.raises(Exception):
        setdefaultservice('default')
    with pytest.raises(Exception):
        setdefaultservice('')
    with pytest.raises(Exception):
        setdefaultservice('xxx')


def test_add_bibformatter():
    """Register a callable under a lowercased name (parity with add_service)."""

    def myfmt(record):
        return 'formatted:%s' % record.get('Title', '')

    add_bibformatter('MyFmt', myfmt)
    assert bibformatters['myfmt'] is myfmt
    assert bibformatters['myfmt']({'Title': 'Hello'}) == 'formatted:Hello'


def test_add_service():
    """Register a query callable under a lowercased name."""

    def myquery(isbn):
        return {'ISBN-13': isbn}

    add_service('MySvc', myquery)
    assert services['mysvc'] is myquery
    assert services['mysvc']('9780446310789') == {'ISBN-13': '9780446310789'}
