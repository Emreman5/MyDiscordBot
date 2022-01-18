import os

DEBUG = os.getenv("DEBUG",False)

if DEBUG:
    from pathlib import Path
    from dotenv import load_dotenv
    env_path = Path(".") / ".env.debug"
    load_dotenv(dotenv_path= env_path)
    from settings_file.development import *
else:
    print("PRODUCTION")
    from settings_file.production import *