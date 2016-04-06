#April 3: Scouting NYPD Stop and Frisk data

**Can you find records relating to Alvin's arrest in 2012? According to reports, it took place on June 3, 2012**

What do we know about Alvin's arrest that can be uased to find his info in the database? Using the [NYPD Stop Question Frisk Database File specifications](http://www.nyc.gov/html/nypd/downloads/excel/analysis_and_planning/2015_sqf_file_spec.xlsx) combined with what we know from news reports:
* his age: 28
* date of stop: 06-03-2011 (reports say 2011, not 2012)
* arrest made? no

Running [this script](https://github.com/readelev/cj-2016/blob/master/week-02/findAlvin.py), we've narrowed down our search to X entries...

This part is unfinished!

**Can you confirm the ratio of innocent people stopped-and-frisked that the NY ACLU reports?**

[The ACLU claims](http://www.nyclu.org/content/stop-and-frisk-data):

In 2010, New Yorkers were stopped by the police 601,285 times.
- 518,849 were totally innocent (86 percent).
- 315,083 were black (54 percent).
- 189,326 were Latino (33 percent).
- 54,810 were white (9 percent).
- 295,902 were aged 14-24 (49 percent).

In 2011, New Yorkers were stopped by the police 685,724 times.
- 605,328 were totally innocent (88 percent).
- 350,743 were black (53 percent).
- 223,740 were Latino (34 percent).
- 61,805 were white (9 percent).
- 341,581 were aged 14-24 (51 percent).

In 2012, New Yorkers were stopped by the police 532,911 times
- 473,644 were totally innocent (89 percent).
- 284,229 were black (55 percent).
- 165,140 were Latino (32 percent).
- 50,366 were white (10 percent).

In 2013, New Yorkers were stopped by the police 191,558 times.
- 169,252 were totally innocent (88 percent).
- 104,958 were black (56 percent).
- 55,191 were Latino (29 percent).
- 20,877 were white (11 percent).

In 2014, New Yorkers were stopped by the police 45,787 times.
- 37,744 were totally innocent (82 percent).
- 24,319 were black (53 percent).
- 12,489 were Latino (27 percent).
- 5,467 were white (12 percent).

In 2015, New Yorkers were stopped by the police 22,939 times.
- 18,353 were totally innocent (80 percent).
- 12,223 were black (54 percent).
- 2,567 were Latino (11 percent).
- 6,598 were white (29 percent).

I pulled the data and ran [this script](https://github.com/readelev/cj-2016/blob/master/NYPD_stopfrisk/ACLUclaimCheck.py). Here's what I found:

*Note 1: the ACLU calculations included only total stops, total innocent and a race breakdown in terms of black, Latino, and white, so I've only included those values.*

*Note 2: the NYPD recorded races of "black hispanic" and "white hispanic", but not "Latino". The ACLU's data for Latino arrests was consistent with the sum of "black hispanic" and "white hispanic" arrests.*

*Note 3: the CSV files for 2011 were in some way corrupted (kept getting error messages), so I've only calculated values from 2012 onward.*

In 2012, New Yorkers were stopped by the police 532911 times.
- 473644 were totally innocent. 89 percent.
- 284229 were black. 53 percent. (This differs from the ACLU value by 2%, or the same value as pestops of race "other". Perhaps the ACLU added these categories?)
- 35772 were black hispanic. 7 percent.
- 129368 were white hispanic. 24 percent.
- 50366 were white. 9 percent.

In 2013, New Yorkers were stopped by the police 191851 times.
- 169662 were totally innocent. 88 percent.
- 104449 were black. 54 percent. (Again, I think the ACLU added the "other" race category to their number.)
- 12271 were black hispanic. 6 percent.
- 42659 were white hispanic. 22 percent.
- 20820 were white. 11 percent.

In 2014, New Yorkers were stopped by the police 45787 times.
- 37744 were totally innocent. 82 percent.
- 24319 were black. 53 percent.
- 2789 were black hispanic. 6 percent.
- 9700 were white hispanic. 21 percent.
- 5467 were white. 12 percent.

In 2015, New Yorkers were stopped by the police 22563 times.
- 18066 were totally innocent. 80 percent.
- 11950 were black. 53 percent.
- 1409 were black hispanic. 6 percent.
- 5090 were white hispanic. 23 percent.
- 2514 were white. 11 percent. (Here, the ACLU's data mixed up Latino and white arrests.)





