# imports - standard imports
import sys, os
import json

# imports - third-party imports
from candis.config   import CONFIG
from candis.resource import R

def main(args = None):
    code = os.EX_OK

    path = os.path.join(R.Path.APP, 'client/app/Config.json')
    dikt = CONFIG.App.schema

    with open(path, 'w') as f:
        json.dump(dikt, f)

    return code

if __name__ == '__main__':
    args = sys.argv[1:]
    code = main(args)

    sys.exit(code)