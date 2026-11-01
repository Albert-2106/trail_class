import runpy, io
from contextlib import redirect_stdout

def test_test_3_output():
    out = io.StringIO()
    with redirect_stdout(out):
        runpy.run_path('test_3.py')
    assert out.getvalue().strip() == "str"
