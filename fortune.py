#coding: cp932
import random
db = []

def db_analyze(fname):
  lines = []
  with open(fname, 'r') as f:
    lines = f.readlines()

  BODY = 1
  AUTH = 2
  NO = 3
  state = NO
  current = [[]]
  for line in lines:
    line = preprocess(line)
    if line.startswith("No."):
      state = NO
    elif line.startswith("by"):
      state = AUTH

    if state == NO:
      state = BODY
    elif state == BODY:
      current[0].append(line)
    elif state == AUTH:
      current.append(line[2:])
      db.append(current)
      current = [[]]

def preprocess(line):
  line = line.strip()
  line = line.replace(" ", "")
  line = line.replace("　", "")
  return line

def get_random_fortune():
  item = random.choice(db)
  body = ''.join(item[0])
  author = item[1]
  return body, author

def get_random_fortune_exclude(ngwords):
  flag = True
  body = ""
  author = ""
  while (flag):
    body, author = get_random_fortune()
    flag = False
    for ngword in ngwords:
      if ngword in body:
        flag = True
        print body
        break
  return body, author