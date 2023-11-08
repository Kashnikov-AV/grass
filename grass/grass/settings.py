from pathlib import Path
import os
import environ
from .base import *

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
env = environ.Env()
if env('SETTINGS') == 'dev':
    from .dev import *
elif env('SETTINGS') == 'prod':
    from .prod import *

