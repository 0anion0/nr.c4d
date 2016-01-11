<h1>
  <span>nr.c4d - Cinema 4D Python Utility Library</span>
  <a href='http://nrc4d.readthedocs.org/en/latest/?badge=latest'>
    <img src='https://readthedocs.org/projects/nrc4d/badge/?version=latest' alt='Documentation Status' />
  </a>
</h1>

> Note: This library was formerly named `c4dtools` and you can find the
> old versions in the Git history at branches `v1.3.0` and `v1.3.1`. 

The `nr.c4d` library provides a toolset for Cinema 4D Python developers
and scripters that contains solutions for common non-simple tasks and
utilities to work with the Cinema 4D API.

Contributions are welcome!

__Overview__

- `nr.c4d.gui`: Utilities for working with the Cinema 4D GUI API
  and implementing custom user interface
- `nr.c4d.math`: A collection of mathematical algorithms commonly
  used in 3D space computations
- `nr.c4d.utils`: Common utility functions
- `nr.c4d.modeling`: Helper class to program C4D modeling operations
  using modeling commands (`c4d.utils.SendModelingCommand`) or modeling
  objects (eg. the "Boole" object)
- `nr.c4d.structures.treenode`: A `c4d.BaseList2D`-like tree
  datastructure (commonly used in a `c4d.gui.TreeViewGui`)
- `nr.c4d.structures.ordereddict`: A dictionary-like datatype that
  supports non-hashable keys (all Cinema 4D node types are unhashable)

__Additional Links__

- [Documentation](https://nrc4d.rtfd.org/)
- [Issue Tracker](https://github.com/nr-python/nr.c4d/issues)
