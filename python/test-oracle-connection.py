#!/usr/bin/env python

import argparse
import cx_Oracle
import requests
import sys

def test_oracle_connection(cursor):
  cursor.execute(
    """SELECT 'Connect to Oracle database successfully at ' ||  TO_CHAR (SYSDATE, 'DD-MON-YYYY HH24:MI:SS') || '!' FROM DUAL"""
  )

  rows = cursor.fetchall()

  for string in rows:
    print('%s' % (string))

  return rows

def parse_args(args):
  parser = argparse.ArgumentParser(description='Testing Oracle connection')
  parser.add_argument('--tns', required=True, help='Oracle TNS Name to connect (You need to have oracle wallet set up)')
  return parser.parse_args(args)

if __name__ == '__main__':
  args = parse_args(sys.argv[1:])

  # dsn: data source name
  # tns: Oracle Wallet's TNS (Transparent Network Substrate) name
  connection = cx_Oracle.connect(dsn=args.tns, encoding="UTF-8")

  # Optional: login using your username and password
  '''
  connection = cx_Oracle.connect(
    user="<your-user>",
    password="<your-password>",
    dsn="<dsn>")
  '''

  cursor = connection.cursor()

  try:
    test_oracle_connection(cursor)
  finally:
    cursor.close()
    connection.close()
