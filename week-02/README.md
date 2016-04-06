# Hey! This is week two.

![img](http://placekitten.com/200/300)

Scripts included in the folder week-02:
* Basic [scraping script](https://github.com/readelev/cj-2016/blob/master/week-02/scraping.py) to download all [this data](http://www.nyc.gov/html/nypd/html/analysis_and_planning/stop_question_and_frisk_report.shtml) from NYPD's stop and frisk program
* [Script to unzip](https://github.com/readelev/cj-2016/blob/master/week-02/unpacker.py) all downloaded files at once

# Homework

## Due Wednesday, 2016-04-06 23:59

# 1. Aggregate and inspect healthcare data breach records

* Download the **CSV** version of data [from the U.S. Department of Health and Human Services Office for Civil Rights database of Breaches Affecting 500 or More Individuals](http://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html)

Find:

* Total the number of individuals affected = 158,027,958.
* Chart showing the number of individuals affected by year.

Year | # individuals affected
---------- | ----------
2009 | 134773
2010 | 5534276
2011 | 13149792
2012 | 2808042
2013 | 6950118
2014 | 12683589
2015 | 113258966
2016 | 3508402

* Attempt to ascertain whether or not electronic records are more prone to violation than non-electronic records.


| Paper | Electronic
----------| ---------- | ----------
# breaches | 343 | 1175
# affected | 373 | 1122

* Paragraph or so explaining why it is difficult to ascertain any paper vs. electronic trend, in terms of pure numbers. This includes thinking about the limitations of the data and how it was collected and recorded.

The data was collected by "Location of Breached Information", which doesn't specify *how* the breach occured, which almost matters more than *where* the breach occured. Like, a computer stolen from a desk is a non-electronic breach in the same way that papers being misplaced/lost are a non-electronic breach: no one downloaded data or hacked into a system in order to get HIPAA data. However, the USDH records the "Location of Breached Information" when a computer is stolen as a "Network Server" breach, the same sort of breach hacking into web servers. 

To make it worse, there's a HUGE variety in what's written down for "Location of Breached Information". In my pivot table, I found 64 different potential values. Many cells wrote in many locations, "Paper/Films" along with "Laptop" or "Email", making it hard to categorize.

This was done in excel, but [here's a scrip that does a simple count](https://github.com/readelev/cj-2016/blob/master/week-02/scrapingHealth.py).


# 2. Aggregate the job losses as recorded by the California WARN act

Python script [here](https://github.com/readelev/cj-2016/blob/master/week-02/jobData.py). The script:

* Downloads all of the PDF WARN reports for California, which can be found here: http://www.edd.ca.gov/jobs_and_training/Layoff_Services_WARN.htm
* Extracts tabular data from each PDF and serializes it as CSV (i.e. saves it as a CSV file). 

Year | Layoffs
---------- | ----------
2012 | 45546
2013 | 58808
2014 | 29306
2014b | 12907
2015 | 68394
2016 | 53787
*Total* | 268748

Total number of California job losses I calculated from 2012 to today = 268,748.

# 3. Download and process a data file from another state's WARN Act

Relevant Python code (for downloading the data) [here](https://github.com/readelev/cj-2016/blob/master/week-02/OhioWARNdata.py)

Year | Layoffs
---------- | ----------
2012 | -
2013 | -
2014 | 7876
2015 | 1563260
**Total** | 1571136

*Note: I have to clean the spreadsheets for 2012 and 2013 before I can use them (due to whitespaces).*

The total number of jobs listed for 2014 and 2015 = 1,571,136.






