# pyblend

### Setup
In the blender Python console, run `import sys; sys.executable` to get the path to the Blender Python binary. Configure your IDE to use this binary as the project interpreter.

Then run the following, replacing `/Applications/.../python3.9` with the path returned by `sys.executable` above:

```
git clone https://github.com/bencbartlett/pyblend.git
/Applications/Blender.app/Contents/Resources/2.93/python/bin/python3.9 -m pip install -e pyblend
```
This will install the package in editable mode and will install the dependencies, including the `fake-bpy-module-2.93` which will provide code completion for `bpy`, `bmesh`, and related modules in an IDE.