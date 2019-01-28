import platform
import pprint

profile = [
    platform.architecture(),
    platform.dist(),
    platform.libc_ver(),
    platform.machine(),
    platform.node(),
    platform.platform(),
    platform.processor(),
    platform.python_build(),
    platform.python_compiler(),
    platform.python_version(),
    platform.system(),
    platform.uname(),
    platform.version(),
]
pprint.pprint(profile)

