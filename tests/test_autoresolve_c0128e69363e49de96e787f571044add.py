import runpy, io
from contextlib import redirect_stdout

def test_test_5_output():
    out = io.StringIO()
    with redirect_stdout(out):
        runpy.run_path('test_5.py')
    assert out.getvalue().strip() == "str"