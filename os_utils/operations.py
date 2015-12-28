import hashlib


def get_md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, 'rb') as file_:
        batch_size = 4096
        chunk = file_.read(batch_size)
        while chunk:
            md5_hash.update(chunk)
            chunk = file_.read(batch_size)

        return hashlib.md5(file_.read()).hexdigest()
