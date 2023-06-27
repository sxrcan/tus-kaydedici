import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["pynput"],
    "excludes": [],
    "include_files": [],
}

exe = Executable(
    script="sercan.py",
    base=None,
)

setup(
    name="sercan",
    version="1.0",
    description="81",
    options={
        "build_exe": build_exe_options,
    },
    executables=[exe],
)
