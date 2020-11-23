from __future__ import annotations

from typing import Dict, Type


def bound(model):
    def wrapper(cls):
        schema_model_mapping[cls] = model
        return cls

    return wrapper


schema_model_mapping: Dict[Type:Type] = {}
