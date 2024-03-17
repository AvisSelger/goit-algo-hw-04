cats_file_path = '/mnt/data/cats_info.txt'
cats_data = """60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5"""

with open(cats_file_path, 'w') as file:
    file.write(cats_data)

cats_file_path


def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cats_list.append({"id": cat_id, "name": name, "age": age})
    except Exception as e:
        print(f"An error occurred: {e}")
    return cats_list

cats_info = get_cats_info(cats_file_path)
cats_info
