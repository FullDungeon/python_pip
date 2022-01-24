from . import version
import argparse


# ---- functions used by the argparser
# names starts with 'p_' (so I can distinguish they from other objects)
def p_version(args):
    print(version)


# ---- arguments definition
def parser():
    p = argparse.ArgumentParser()
    s = p.add_subparsers(help='commands')

    version_parser = s.add_parser('version', help='print package version')
    version_parser.set_defaults(func=p_version)

    '''
    PARAMETERS EXAMPLES
    
    # ---- parameter with alias (without value)
    example_parser.add_argument('--long', '-l', default=False, action='store_true')
    
    # ---- parameter with value (without alias)
    example_parser.add_argument('value', default='.')
    
    '''

    return p


# ---- entry point
def run():

    p = parser()
    args = p.parse_args()

    if not hasattr(args, 'func'):
        p.print_help()
    else:
        args.func(args)
        return 0

    return 1
