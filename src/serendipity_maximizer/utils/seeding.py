"""Reproducibility helpers."""

import os
import random


def set_global_seed(seed: int = 42) -> None:
    """Set seeds for python random (extend for numpy/torch if added)."""
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
