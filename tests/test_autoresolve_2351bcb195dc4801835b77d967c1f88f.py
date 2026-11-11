import runpy, io
from contextlib import redirect_stdout

def test_test_7_output():
    out = io.StringIO()
    with redirect_stdout(out):
        runpy.run_path('test_7.py')
    assert out.getvalue().strip() == "9"