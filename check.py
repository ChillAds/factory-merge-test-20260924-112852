from pathlib import Path
import subprocess
print("tested_commit_sha="+subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip())
if Path("impl.py").exists():
    assert subprocess.check_output(["python3","impl.py"],text=True).strip()=="ok"
print("CHECK_OK")
