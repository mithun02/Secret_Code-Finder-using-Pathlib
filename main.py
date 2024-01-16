from pathlib import Path
import re

cwd=Path.cwd()
cwd

target_dir=cwd / "directory" 
for file in target_dir.rglob("*.txt"):
    file_cont= file.read_text()
    search=re.search("Secret Code:(.+)",file_cont)

    if search:
        secret_code=search.group(1)
        print("File:",file,"Secret Code:",secret_code)
    else:
        print("Not Found")    
