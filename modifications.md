# Potential Modifications

This document lists the modifications made from the originally published benchmark.

## Setup.py

We added a `setup.py` file so that it's possible to install `aerobench` as a package.
It can now be installed from the root of the repository with the following command.

```
pip install -e code/
```

There is then no need to modify `PYTHONPATH`.

## Initial State Representation

One of the main difficulties in working with the code as it is that the state is represented with a list requiring a magical and forgettable mapping from indices to variables.
This makes the code hard to read and modifications hard to write.

Design goals:
- Backward compatible.
- Self-documenting.

## Output Representation
