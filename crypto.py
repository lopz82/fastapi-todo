import bcrypt


def hash_password(password: str, encoding: str = "utf-8") -> str:
    encoded = bytes(password.encode(encoding))
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())
    return hashed.decode(encoding)


def is_correct_password(password: str, hashed: str, encoding: str = "utf-8") -> bool:
    encoded_passwd = bytes(password.encode(encoding))
    encoded_hash = bytes(hashed.encode(encoding))
    return bcrypt.checkpw(encoded_passwd, encoded_hash)
