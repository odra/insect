import sys

import pip
import pytest

import insect


def test_is_installed():
  assert insect.is_installed('requests') is False


def test_install():
  insect.install('requests')
  assert insect.is_installed('requests') is True


def test_load():
  req = insect.load('requests')
  assert 'requests' in sys.modules.keys()


def test_module():
  req = insect.load('requests')
  assert req.get('https://www.google.com').status_code == 200
