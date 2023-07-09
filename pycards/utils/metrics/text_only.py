from difflib import SequenceMatcher


def string_ratio(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()
