def update_dict(a: dict, b: dict):
    for k, v in a.items():
        if k in b and b.get(k, None):
            a[k] = b[k]
