import sys

has_error = False

def main():
    try:
        import exercise1

        if not hasattr(exercise1, 'name'):
            error("Cannot find 'name' variable in exercise1.py")

        print_unless_error("Everything looks good. Nice job.")

    except:
        error("Cannot load exercise1.py")

def error(message):
    global has_error
    has_error = True
    print(message, file=sys.stderr)


def print_unless_error(message):
    if has_error:
        error("There were errors. Please fix them.")
    else:
        print(message)


if __name__ == '__main__':
    main()
