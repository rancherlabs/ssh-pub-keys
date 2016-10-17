#!/usr/bin/env python3

import os, sys, re, colorama

from colorama import Fore, Style, Back
from invoke import run, Failure


colorama.init()


#
def log_info(msg):
    print(Back.BLACK + Fore.WHITE + msg + Fore.RESET)


#
def log_debug(msg):
    print(Back.BLACK + Fore.BLUE + msg + Fore.RESET)


#
def log_error(msg):
    sys.stderr.write(Back.BLACK + Style.BRIGHT + Fore.RED + msg + os.linesep + Fore.RESET + Style.NORMAL)


#
def claxon_and_exit(msg):
    # blink text does not work for many TERMs :\
    sys.stderr.write(Back.RED + Style.BRIGHT + Fore.WHITE + msg + os.linesep + Fore.RESET + Style.NORMAL)
    sys.exit(-10)


#
def log_success(msg):
    print(Back.BLACK + Style.BRIGHT + Fore.GREEN + msg + Fore.RESET + Style.NORMAL)


#
def err_and_exit(msg):
    log_error(msg)
    sys.exit(-1)


#
def debug_mode():
    if os.environ.get('DEBUG'):
        return True
    else:
        return False


#
def validate_ssh_pub_key(line):
    """
    Validate the line passed as a valid pub key for user in authorized_keys* file.
    This needs massive improvmement but is a 'good enough' start.
    """

    ssh_pub_key_re = '^(ssh\-dss|ssh\-rsa|ecdsa\-sha2\-nistp256|ecdsa\-sha2\-nistp384|ecdsa\-sha2\-nistp521).+$'
    mo = re.match(ssh_pub_key_re, line)
    if debug_mode():
        log_debug("Checking \'{}\' against re \'{}\'.".format(line, ssh_pub_key_re))
    if mo:
        return True
    else:
        log_error("Failed to validate line \'{}\' against regex \'{}\'!".format(line, ssh_pub_key_re))
        return False


#
def check_file(keysfile):
    log_info("Checking \'{}\'...".format(keysfile))

    result = True
    lineno = 0
    try:
        with open(keysfile,'r') as f:
            for line in f:
                lineno += 1
                line = line.rstrip()
                if 'PRIVATE KEY' in line:
                    log_error("File \'{}\' appears to contain a private key!".format(keysfile))
                    claxon_and_exit("If this key is present in a git push or pull request it should now be considered compromised as it appears in the ref log in the public repository!")
                if debug_mode():
                    log_debug("Checking key at line {}...".format(lineno))
                if False is validate_ssh_pub_key(line):
                    log_error("Failed to validate line \'{}\' in file \'{}\' against regex \'{}\'!".format(line, keysfile))
                    return False
    except IOError as e:
        log_error("Failed on open() for \'{}\' :: {} :: {}".format(
            keysfile,
            e.errno,
            e.strerror))
        return False

    return True


#
def check_dir(keyspath):
    result = True

    for root, dirs, files in os.walk(keyspath, topdown=False):
        if debug_mode():
            log_debug("Checking: root: {}, dir: {}, files: {}...".format(root, dirs, files))

        for f in files:
            if False is check_file("{}/{}".format(root, f)):
                result = False

    return result


#
def main():
    keydir = './ssh-pub-keys'


    log_info("Checking contents of \'{}\'...".format(keydir))
    run("tree {}".format(keydir))

    if False is check_dir(keydir):
        err_and_exit('Failed while checking SSH keys!')
    else:
        log_success('Key files look good.')


if '__main__' == __name__:
    main()
