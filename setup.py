#!/usr/bin/python3

"""
Packaging module
"""

import os
import sys
import zipapp


module_name = "pyweb.pyz"
interpreter = "python"
if os.name == "posix":
    interpreter = "python3"


def execute(*args):
    """
    @param *args system command
    """
    cmd = " ".join(args)
    ret = os.system(cmd)
    if ret != 0:
        print("Execution failed for [%s]! " % cmd, file=sys.stderr)
        sys.exit(ret)


def cmd_execute(*args):
    """
    Document package
    Generate package
    @param *args parameters
    """
    args = list(*args)
    pars = None
    if "run" in args:
        pars = [interpreter, module_name]
        pars.extend(args[args.index("run") + 1:])
        args = args[:args.index("run")]
    if len([
            arg for arg in args
            if arg not in ["-h", "pep8", "doc", "install", "ssl"]]) > 0:
        raise Exception(
            "Command not in: [pep8] [doc] [install] [ssl] [run [args]]")
    if "-h" in args:
        print("arguments [no] [pep8] [doc]")
    if "pep8" in args:
        execute("pep8", ".", "src")
        print("%s check styled" % module_name)
    if "doc" in args:
        execute(interpreter, "-B", "src/doc.py", ".", "src")
        print("%s documented" % module_name)
    if "install" in args:
        zipapp.create_archive("src", target=module_name)
        os.makedirs("work", exist_ok=True)
        print("%s generated" % module_name)
    if "ssl" in args:
        execute(
            "openssl", "req", "-x509", "-sha256", "-nodes", "-days", "365",
            "-newkey", "rsa:2048",
            "-keyout", "work/privateKey.key",
            "-out", "work/certificate.crt")
    if pars is not None:
        execute(*pars)


def main_function():
    "Main function"
    if len(sys.argv) < 2:
        print("Available commands: [pep8] [doc] [install] [ssl] [run [args]]")
        print("Empty line to quit")
        print("================")
        line = sys.stdin.readline()
        while line != "\n":
            cmd_execute(line[:-1].split(" "))
            line = sys.stdin.readline()
        print("Bye!")
        print("================")
    else:
        cmd_execute(sys.argv[1:])


if __name__ == "__main__":
    main_function()
