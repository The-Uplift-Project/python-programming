import platform
import os
import sys

print("Machine network name:", platform.node())
print("Python version:", platform.python_version())
print("System:", platform.system())
print("USERNAME environment variable:", os.environ["USERNAME"])
