from pathlib import Path
import random
import string

BASE_DIR = Path()

no_dir = random.randint(30, 100)
file_path_index = random.randint(30, no_dir)
file_path = None

characters = list(string.ascii_letters+string.digits+string.punctuation)

random.shuffle(characters)
secret_code = "".join([
    random.choice(
        characters
        ) for i in range(random.randint(12, 24))
])

for i in range(1, no_dir+1):
    directory = BASE_DIR / f"directory-{i}"
    directory.mkdir(exist_ok=True)
    if i == file_path_index:
        file = (directory / "FINDME.txt")
        file.touch(exist_ok=True)
        file_path = file


with open(file_path.absolute().as_posix(), "w") as f:
    f.write(f"Secret Code: {secret_code}")
