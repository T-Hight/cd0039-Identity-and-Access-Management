#!c:\users\taylo\udacity\cd0039-identity-and-access-management\project\03_coffee_shop_full_stack\starter_code\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'jose==1.0.0','console_scripts','jose'
__requires__ = 'jose==1.0.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('jose==1.0.0', 'console_scripts', 'jose')()
    )
