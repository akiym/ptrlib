import os
import subprocess
from typing import Optional


def which_linux(s: str) -> Optional[str]:
    if '/' not in s:
        try:
            s = subprocess.check_output(["which", s]).decode().rstrip()
        except subprocess.CalledProcessError:
            s = None
    elif not os.path.isfile(s):
        s = None
    return s
