# wslsubl

Transparent bridge to interact with a Windows installation of Sublime Text from within a WSL environment.

## Requirements

[wslpy](https://wslutiliti.es/wslpy/)

## Installation

From within WSL:

```
cd /usr/local/bin
ln -s {REPO DIR}/subl.py subl
```

## Usage

Use as you normally would invoke `subl` from a terminal:

`subl.py [arguments] [files]`

Paths are automatically converted from WSL to Windows syntax via [wslpy](https://wslutiliti.es/wslpy/).

## TODO

- Currently, the script expects Sublime to be installed to `"C:\Program Files\Sublime Text\"`. This should either be parameterizable via environment variable or, preferably, auto-detected.