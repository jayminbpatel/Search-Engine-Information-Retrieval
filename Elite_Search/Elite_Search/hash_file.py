import hashlib

def get_hash(file_path, file_name):
    hasher = hashlib.md5(file_name)
    return hasher.hexdigest()
def hash_filepath(filepath):
    hasher = hashlib.md5(filepath)
    return hasher.hexdigest()