import runpy, io
from contextlib import redirect_stdout

def test_test_py_fixed():
    out = io.StringIO()
    with redirect_stdout(out):
        runpy.run_path('test.py')
    assert out.getvalue().strip() == "3a"
