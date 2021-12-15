from pathlib import Path
import shutil
import os
import filecmp

originalFile = Path("snek!.py")
pywFile = Path("snek!.pyw")

# create python script without console if there is no script without console or
# script without console and original script are not equal
if not pywFile.is_file() or not filecmp.cmp(originalFile, pywFile, False):
    shutil.copy(originalFile, pywFile)

os.startfile(pywFile)
exit()
