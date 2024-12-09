#!/usr/bin/env python
"""
moonphase.py - Calculate Lunar Phase
Author: Sean B. Palmer, inamidst.com
Cf. http://en.wikipedia.org/wiki/Lunar_phase#Lunar_phase_calculation
"""

import sys, math, decimal, datetime
dec = decimal.Decimal

offset = dec("0.20439731")
# the lunations at jan 1, 2001
lunations_per_day = dec("0.03386319269")

def position(now=None): 
   if now is None: 
      now = datetime.datetime.now()

   diff = now - datetime.datetime(2001, 1, 1)
   days = dec(diff.days) + (dec(diff.seconds) / dec(86400))
   lunations = offset + (days * lunations_per_day)

   return lunations % dec(1)

def phase(index): 
   return {
      0: "New Moon", 
      1: "Waxing Crescent", 
      2: "First Quarter", 
      3: "Waxing Gibbous", 
      4: "Full Moon", 
      5: "Waning Gibbous", 
      6: "Last Quarter", 
      7: "Waning Crescent"
   }[int(index) & 7]

def next_quarter(): 
   now = datetime.datetime.now()
   
   diff = now - datetime.datetime(2001, 1, 1)
   days = dec(diff.days) + (dec(diff.seconds) / dec(86400))
   lunations = offset + (days * lunations_per_day)
   
   quarter_type = phase(math.ceil(lunations * 4) * 2)
   next_quarter = math.ceil(lunations * 4)
   # the upcoming quarter is the nth since 2001.
   lunations = dec(next_quarter / 4.) - offset
   days = lunations / lunations_per_day
   
   date_of_quarter = datetime.datetime(2001, 1, 1) + datetime.timedelta(days=float(days))
   return (date_of_quarter, quarter_type)

def main(): 
   if len(sys.argv) == 1:
      pos = position()

      roundedpos = round(float(pos), 3)
      print("%s" % (roundedpos))
   else:
      (date,name) = next_quarter()

      print("%s at %s|%s-%s;%s:%s_%s" % (name, date.year, '{0:02}'.format(date.month), '{0:02}'.format(date.day), '{0:02}'.format(date.hour), '{0:02}'.format(date.minute), '{0:02}'.format(date.second)))
   

if __name__=="__main__": 
   main()
