# import방법

* notebook의 이름을 module로 씁니다.
* notebook안에 import시 실행될 코드들의 맨 위에 `#import`를 넣습니다.
* import할 notebook에서
  * `import nbook`을 실행한 이후 import하면 됩니다.
 
## Origin

This was started as an import module by [Adrian Price-Whelan][0], concatenated by [Robert Clewley][1], updated by [Doug Callaway][2], and finally recycled for an interactive console by me. 

[0]: http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Importing%20Notebooks.html
[1]: https://gist.github.com/robclewley/75b7719119892b99d73b
[2]: https://gist.github.com/DCAL12/1a872bd63bedfb7b12612c8a7ec0f52e

## Installation

```
git clone https://github.com/thejohnhoffer/ipynb.git
pip install -e ipynb
```
