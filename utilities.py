import sys, os

if os.environ.get("DEBUG", "") in ("yes", "y", "true", "True"):
    DEBUG=True
else:
    DEBUG = False

def DEBUG_PRINT(*arguments):
    if DEBUG:
        print(*arguments, file=sys.stderr)
