import importlib
import importlib.util

import pip


def install(name, version=None):
  args = [
    'install',
    name,

  ]
  if version:
    args[1] = '%s==%s' % (args[1], version)
  pip.main(args)


def is_installed(name):
  if importlib.util.find_spec(name):
    return True
  return False


def load(name, version=None, url=None):
  if is_installed(name):
    return importlib.import_module(name)
  if url is None:
    install(name, version)
  else:
    install(url)
  return importlib.import_module(name)
