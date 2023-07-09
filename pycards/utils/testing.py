from contextlib import contextmanager
import sys


@contextmanager
def replace_stdin(target):
    original = sys.stdin
    sys.stdin = target
    yield
    sys.stdin = original
