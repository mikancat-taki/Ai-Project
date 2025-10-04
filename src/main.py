import sys
from app import start_application

if __name__ == "__main__":
    try:
        start_application()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)