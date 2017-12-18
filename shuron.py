#coding: cp932
import datetime as d
import fortune as f

def progress(ratio):
  start = '['
  end = ']'
  done = '|'
  yet = '.'
  length = 60
  result = start
  for i in xrange(0,length):
    if (i+1<=ratio*length):
      result += done
    else:
      result += yet
  result += end
  return result

if (__name__ == "__main__"):
  start = d.date(2017,11,1)
  target = d.date(2018,2,5)
  diff = (target - d.date.today()).days
  orgdiff = (target-start).days
  rate = 1-diff*1./orgdiff
  
  f.db_analyze('db.txt')
  #body, author = f.get_random_fortune()
  ngwords = ["恋","愛","／","金","悪","死","女","男","戦争","友","自由","売","買","歴史","法律"]
  body, author = f.get_random_fortune_exclude(ngwords)

  with open("shuron.properties", 'w') as f:
    f.write("SHURON_ORG_DAY = {0}".format(orgdiff))
    f.write("\n")
    f.write("SHURON_DAY = {0}".format(diff))
    f.write("\n")
    f.write("SHURON_WEEK = {0:.1f}".format(diff/7.))
    f.write("\n")
    f.write("SHURON_RATE = {0:.1f}".format(rate*100))
    f.write("\n")
    f.write("SHURON_RATE_STR = {0}".format(progress(rate)))
    f.write("\n")
    f.write("SHURON_FORTUNE_BODY ={0}".format(body))
    f.write("\n")
    f.write("SHURON_FORTUNE_AUTHOR ={0}".format(author))

