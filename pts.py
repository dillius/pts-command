#!/usr/bin/env python
import argparse
import json
import urllib.parse
import urllib.request


def main():
    p = argparse.ArgumentParser()
    p.add_argument("user",
                   help="Username on peaktolerablestupidity; ex: Jim",
                   type=str)
    p.add_argument("-c",
                   "--change",
                   type=str,
                   help="Value to set tolerance level to or modification" +
                        " to perform to existing value; ex: 20, 35, +10")
    args = p.parse_args()
    if args.change:
        update_user(args.user, args.change)
    else:
        get_user(args.user)


def get_user(user):
    url = "http://www.peaktolerablestupidity.com/api/entry/{0}".format(user)
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    result = json.loads(resp.read().decode('ascii'))
    if result:
        print("{0} is at tolerance level: {1}".format(user, result['level']))
    else:
        print("{0} is not currently registered".format(user))


def update_user(user, change):
    url = "http://www.peaktolerablestupidity.com/api/entry"
    values = {'user': user,
              'level': change}
    data = urllib.parse.urlencode(values)
    binary_data = data.encode('ascii')
    req = urllib.request.Request(url, binary_data)
    resp = urllib.request.urlopen(req)
    result = json.loads(resp.read().decode('ascii'))
    print("{0} now at tolerance level: {1}".format(user, result['level']))


if __name__ == '__main__':
    main()
