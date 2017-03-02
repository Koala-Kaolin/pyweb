#!/usr/bin/python3

"""
Packaging module
"""

import os
import sys
import zipapp

module_name = "pyweb.pyz"
interpreter = "python3"


is_linux = False
is_windows = False
if os.name == "posix":
    is_linux = True
else:
    is_windows = True


def execute(*args):
    """
    @param *args system command
    """
    cmd = " ".join(args)
    ret = os.system(cmd)
    if ret != 0:
        print("Execution failed for [%s]! " % cmd, file=sys.stderr)
        sys.exit(ret)


def cmd_install(*args):
    """
    Document and generate package
    @param *args parameters
    """
    cmd_document(*args)
    cmd_package(*args)


def cmd_package(*args):
    """
    Generate package
    @param *args parameters
    """
    zipapp.create_archive("src", target=module_name)
    os.makedirs("work", exist_ok=True)
    print("%s generated" % module_name)


def cmd_document(*args):
    """
    Document package
    @param *args parameters
    """
    execute("pep8", ".", "src")
    execute(interpreter, "-B", "src/doc.py", ".", "src")
    print("%s documented" % module_name)


def cmd_ssl(*args):
    """
    Generate a certificate
    @param *args parameters
    """
    execute(
        "openssl", "req", "-x509", "-sha256", "-nodes", "-days", "365",
        "-newkey", "rsa:2048",
        "-keyout", "work/privateKey.key", "-out", "work/certificate.crt")


def cmd_run(args):
    """
    Run the server
    @param args parameters
    """
    pars = [interpreter, module_name]
    pars.extend(args)
    execute(*pars)


commands = {
    "install": cmd_install,
    "package":  cmd_package,
    "document":  cmd_document,
    "ssl": cmd_ssl,
    "run": cmd_run
}


def usage():
    "Help"
    print("Available commands: \n\t%s" % "\n\t".join(list(commands.keys())))
    sys.exit(-1)


def main_function():
    "Main function"
    if len(sys.argv) < 2:
        usage()
    cmd = sys.argv[1]
    if cmd not in commands:
        usage()
    else:
        commands[cmd](sys.argv[2:])


if __name__ == "__main__":
    main_function()
