#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dirname):
  """Given a directory name, returns a list of absolute paths 
  of special files (containing __w__) in that directory."""
  result = []
  filenames = os.listdir(dirname)
  for filename in filenames:
    if re.search(r'__\w+__', filename):
      fullpath = os.path.abspath(os.path.join(dirname, filename))
      result.append(fullpath)
  return result

def copy_to(paths, todir):
  """Given a list of file paths, copies those files into todir,
  creating todir if it does not already exist."""
  if not os.path.exists(todir):
    os.makedirs(todir)
  for path in paths:
    shutil.copy(path, todir)

def zip_to(paths, zippath):
  """Given a list of file paths, zips those files up into zippath 
  using an external zip command."""
  cmd = ['zip', '-j', zippath] + paths
  print("Command I'm going to do:", " ".join(cmd))
  
  process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  if process.returncode != 0:
    if process.stdout:
      print(process.stdout.decode('utf-8'))
    if process.stderr:
      print(process.stderr.decode('utf-8'), file=sys.stderr)
    sys.exit(process.returncode)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print('usage: [--todir dir][--tozip zipfile] dir [dir ...]')
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if not args: # A zero length array evaluates to "False".
    print('error: must specify one or more dirs')
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  paths = []
  for dirname in args:
    paths.extend(get_special_paths(dirname))

  if todir:
    copy_to(paths, todir)
  elif tozip:
    zip_to(paths, tozip)
  else:
    for path in paths:
      print(path)

if __name__ == '__main__':
  main()
