import hashlib

def get_hash(file_path, file_name):
    hasher = hashlib.md5(file_name)
    return hasher.hexdigest()