#!/usr/bin/env python
import argparse
import json
import urllib.parse
import urllib.request


def main():
    p = argparse.ArgumentParser()
    p.add_argument('user')
    p.add_argument('change')
    args = p.parse_args()
    update_user(args.user, args.change)


def update_user(user, change):
    url = "http://www.peaktolerablestupidity.com/api/entry"
    values = {'user': user,
              'level': change}
    data = urllib.parse.urlencode(values)
    binary_data = data.encode('ascii')
    req = urllib.request.Request(url, binary_data)
    resp = urllib.request.urlopen(req)
    result = json.loads(resp.read().decode('ascii'))
    print("{0} now at toleration level: {1}".format(user, result['level']))


if __name__ == '__main__':
    main()