#!/usr/bin/env python3

import argparse
import sys
import uuid
from netaddr import EUI
from datetime import datetime
import math
import struct
import hashlib

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate a Unique Local Address'
    )
    parser.add_argument('-m', '--mac', help='MAC address',
                        default=uuid.getnode())
    args = parser.parse_args()

    try:
        eui48 = EUI(args.mac)
    except Exception as err:
        print('{}: {}'.format(parser.prog, err), file=sys.stderr)
        sys.exit(1)
    else:
        eui64 = eui48.modified_eui64()

    now = datetime.utcnow()
    start = datetime(1900, 1, 1, 0, 0, 0)
    delta = (now - start).total_seconds()
    subsec, sec = math.modf(delta)
    ntpstamp = (int(sec) << 32) + int(subsec * 0xffffffff)

    key = eui64.packed + struct.pack('Q', ntpstamp)
    id = hashlib.sha1(key).hexdigest()[-10:]
    print('fd{}:{}:{}::/48'.format(id[0:2], id[2:6], id[6:10]))
    sys.exit(0)
