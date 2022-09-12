# wslsubl

Transparent bridge to interact with a Windows installation of Sublime Text from within a WSL environment.

## Requirements

[wslpy](https://wslutiliti.es/wslpy/)

## Installation and configuration

From within WSL:

```
cd /usr/local/bin
ln -s {REPO DIR}/subl.py subl
```

The script searches for the Windows installation of Sublime Text in `/mnt/c/Program Files` and `/mnt/c/Program Files (x86)`. If Sublime is installed elsewhere, you can explicitly point it to `subl.exe` with the `SUBLIME_PATH` environment variable.

## Usage

Use as you normally would invoke `subl` from a terminal:

`subl.py [arguments] [files]`

Paths are automatically converted from WSL to Windows syntax via [wslpy](https://wslutiliti.es/wslpy/).

