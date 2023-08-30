# COMPAS UI Plugin Template

A minimal example of creating a compas_ui based Rhino plugin.

To use this template:

Both in source code and file path,
1. Change all occurrences of `compas_extension` to your wanted python package name.
2. Change all occurrences of `PLUGIN_NAME` to the name you want to use for the Rhino plugin.


To install:
```
pip install -e .
python -m compas_rhino.install
```

Then in Rhino menu bar, at Tools > Toolbar Layout > File > Open :
You should see a generated `PLUGIN_NAME.rui` for loading the Plugin menu. 