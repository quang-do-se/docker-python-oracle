#!/usr/bin/env python

import argparse
import cx_Oracle
import requests
import sys

def test_oracle_connection(cursor):
  cursor.execute("""SELECT 'Connect to Oracle: ' || 'Successful!' FROM DUAL""")

  rows = cursor.fetchall()

  for string in rows:
    print('%s' % (string))

  return rows

def parse_args(args):
  parser = argparse.ArgumentParser(description='Testing Oracle connection')
  parser.add_argument('--url', required=True, help='Oracle lmsmanager connection string')
  return parser.parse_args(args)

if __name__ == '__main__':
  args = parse_args(sys.argv[1:])
  conn = cx_Oracle.connect(args.url)
  cursor = conn.cursor()

  try:
    test_oracle_connection(cursor)
  finally:
    cursor.close()
    conn.close()
