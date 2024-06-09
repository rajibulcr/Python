from pathlib import Path
from rembg import remove, new_session

session = new_session()

for file in Path('.').glob('image.png'):  # Assuming file is in the current directory
    input_path = str(file)
    output_path = str(file.parent / (file.stem + ".out.webp"))

    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input_data = i.read()
            output_data = remove(input_data, session=session)
            o.write(output_data)