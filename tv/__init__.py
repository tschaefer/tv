#!/usr/bin/env python

import argparse
from service import Service

def parse_options():
    parser = argparse.ArgumentParser(description='omxdcli')
    parser.add_argument('-H', '--host',
                        type=unicode,
                        default='localhost',
                        help='bind to address')
    parser.add_argument('-p', '--port',
                        type=int,
                        default=8090,
                        help='listen to port')
    return parser.parse_args()

def run(args):
    service = Service(host=args.host, port=args.port)
    service.run()

def main():
    args = parse_options()
    run(args)

if __name__ == '__main__':
    main()
