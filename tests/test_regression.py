import runpy
import io
from contextlib import redirect_stdout

def test_concatenation_output():
    f = io.StringIO()
    with redirect_stdout(f):
        runpy.run_path('test.py')
    assert f.getvalue().strip() == '3a'