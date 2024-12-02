# %% [markdown]
# # Importing modules from sibling folders
# ## Introduction

# This notebook demonstrates how to import modules from sibling folders in Python. 
# The code cells below show how to import modules from sibling folders in a Jupyter notebook and in a Python script.
# Here is the folder structure of the project:
# ```
# project
# ├── src
# │   ├── folder_A
# │   │   ├── __init__.py
# │   │   ├── Aa.py
# │   │   |── A.py
# │   ├   └── sub_folder_in_folder_A
# │   │       ├── __init__.py
# │   │       └── AA.py
# │   └── folder_B
# │       ├── __init__.py
# │       |── B.py
# │       └── sub_folder_in_folder_B
# │           ├── __init__.py
# │           └── BB.py
# ```

# ## Outline of the solution
# The solution involves adding `__init__.py` files to the folders to make them packages and then 
# modifying the Python sys.path to include the src directory, so that Python can find the modules in the sibling folders, as packages.

# Note the syntax for importing modules from sibling folders (packages) assceesible through the parent folder added to sys.path.
# Also note, the possibility to import modules from subfolders of the sibling folders, as long as they are packages.

# The code cells below demonstrate how to import modules from sibling folders in a Jupyter notebook and in a Python script.
# This solution works in both Jupyter notebooks and Python scripts (to be executed from command-line, etc.).

# This notes is based on the following sources:
# https://www.perplexity.ai/search/with-python-programming-i-have-DJNoN7lOSJWkvG5t3BrgFA
# %%
import os
import sys

from Aa import pi # import the pi variable from the Aa module in the same folder_A package

from pathlib import Path

def enable_import_from_sibling_folders():
    # Add the src directory to the Python path
    src_dir = str(Path(__file__).resolve().parent.parent)
    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)

enable_import_from_sibling_folders()

def is_running_in_jupyter():
    try:
        __IPYTHON__
        return True
    except NameError:
        return False

in_jupyter = is_running_in_jupyter()

if in_jupyter:
    print("Executed from a Jupyter code cell in VS Code.")
else:
    print("Not executed from a Jupyter code cell.")
for path in sys.path:
    print(path)

from folder_B.B import pi as pi_B
from folder_A.sub_folder_in_folder_A.AA import hello as hello_from_sub_folder_in_folder_A_AA
from folder_B.sub_folder_in_folder_B.BB import hello as hello_from_sub_folder_in_folder_B_BB

print(f"Value of pi from module folder_A.Aa: {pi}")
print(f"Value of pi from module folder_B.B: {pi_B}")

print(hello_from_sub_folder_in_folder_A_AA)
print(hello_from_sub_folder_in_folder_B_BB)

# %%