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

* **Total** number of individuals affected = **158,027,958**.
* Chart showing the number of individuals affected by year:

Year | # individuals affected
---------- | ----------
2009 | 134,773
2010 | 5,534,276
2011 | 13,149,792
2012 | 2,808,042
2013 | 6,950,118
2014 | 12,683,589
2015 | 113,258,966
2016 | 3,508,402

* Attempt to ascertain whether or not electronic records are more prone to violation than non-electronic records.

For this prompt, I used the USDH's classification "Location of Breached Information" to determine if the breaches involved paper or electronic records. The "Location" category had a million different potential values, including: Network server, email, paper/films, desktop computer, etc. (In my pivot table, I found 64 different potential values.) For the purpose of this assignment, if the "Location" category contained any mention of paper/films, I included the breach under "Paper". All other breaches fell under "Electronic". Anything with location "other" or "unknown" was not included in either category, but counted as part of the total.

comparison | Paper | Electronic
----------| ---------- | ---------- 
# breaches | 381 (25%) | 970 (64%)
# affected | 2,984,622 (1.9%) | 14,381,1574 (91 %)

I found that that electronic records had more breaches than non-electronic records (only 25% of breaches involved any sort of paper records), but it was impossible to make any sort of useful comparison between paper vs. electronic because of the way the data was collected.

My classification of "paper" versus "electronic" is derived from USDH's "Location" column, which doesn't specify *how* the breach occured. The *how* matters much more than *where*, for example, USDH classifies a breach that occured when a computer was stolen off a desk as an "electronic breach" because the data was located on a computer. This means "electronic" breaches, according to USDH, do not mean a system was hacked but rather the data was located on some sort of electronic device. So we can't use this to draw conclusions as to whether electronic records are more prone to violation than paper records.

(Cleaned spreadsheet with column delineating Paper/Electronic can be found [here](https://github.com/readelev/cj-2016/blob/master/week-02/breach_report_CLEANED.csv))

This was done in excel, but [here's a script that does a simple count](https://github.com/readelev/cj-2016/blob/master/week-02/scrapingHealth.py).


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

CSV's [here](https://github.com/readelev/cj-2016/blob/master/week-02/CA_Data).

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

Downloaded CSV's [here](https://github.com/readelev/cj-2016/blob/master/week-02/Ohio_Data) plus the cleaned CSV's for [2012]() and [2013]().

The total number of jobs listed for 2014 and 2015 = 1,571,136.






