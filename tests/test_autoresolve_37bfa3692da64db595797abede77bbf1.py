import runpy, io
from contextlib import redirect_stdout

def test_test_3_output():
    out = io.StringIO()
    try:
        with redirect_stdout(out):
            runpy.run_path('test_3.py')
    except Exception:
        assert False, "test_3.py raised an exception"
    assert out.getvalue().strip() == "str"
