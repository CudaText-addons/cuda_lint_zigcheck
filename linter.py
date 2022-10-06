from cuda_lint import Linter
from cuda_lint.util import STREAM_STDERR

class ZigCheck(Linter):
    regex = r'^(?P<filename>\<stdin\>|[^\s\:]+):(?P<line>\d+):(?P<col>\d+):\s+error:\s+(?P<message>.*)$'
    multiline = False
    syntax = 'Zig'
    error_stream = STREAM_STDERR
    cmd = ('zig', 'ast-check', '--color', 'off')
