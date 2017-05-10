# Instect

Insect enables you to auto-install modules byt importing them into your code, no need to run pip or easy_install to do so.

Ideal for quick scripts where you do not need/want to manually install packages.

It uses pip to install packages, supporting versioning and installing from URLs as well.

I don't think it works with python 2 ;)

## Installation

Its ironic, I know, but you need to install insect with pip first!


```sh
pip install insect

```

## Docs

There is a full example in "example.py" file.

You only need to import insect and call the `load` function to import and install a package and you are done!


```py
import insect

requets = insect.load('requests') #same as import requests

print(requests.get('http//www.google.com').text)
```


```py
import insect

requets = insect.load('requests', version='')

print(requests.get('http//www.google.com').text)
```


```py
import insect

requests = load('requests', url='https://github.com/kennethreitz/requests/archive/master.zip')

print(requests.get('http//www.google.com').text)
```

```py
import insect

requests = load('requests', url='git+https://github.com/kennethreitz/requests.git')

print(requests.get('http//www.google.com').text)
```


```py
import insect

requests = load('requests', url='git+ssh://git@github.com/kennethreitz/requests.git')

print(requests.get('http//www.google.com').text)
``


## License

MIT license.

Copyright 2017 Leonardo Rossetti <me@lrossetti.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

