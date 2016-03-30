#Data Portal Comparison

(First time using GitHub, so apologies if this is rough.)

##data.gov

194,758 datasets.

Not to start on a negative note, but **data.gov** seemed to be the worst of the five data portals. Searching for data related to "janitor" gave me no results, while "janitorial" gave one result. Seems like that dataset should be able to be found under both queries.

As far as pros, I appreciated being able to narrow my search criteria. For example, I searched "university acceptance" and could filter by "Dataset type" (geospatial or non-geospatial) or "Organization type" (Feds, State level), but that was about it in terms of helpful filters. "Topic" and "Topic category" did nothing for me.

I particularly liked the first sentence of their "Impact" Tab, which seemed to function like an "About" page might:
>"Open government data is important because the more accessible, discoverable, and usable data is, the more impact it can have."

And then there's the...
>Submit impact suggestions here.

##Open Data Networt##

104,194 results.

*Pros:*

**Open Data Network** has this handy feature where the show you "Sample Values" in each column, which made it really easy to understand the level of detail / usability in each dataset.

*Cons:*

Had the same issue (as data.gov) of not including search results for "janitor" within results for "janitorial". Also, Open Data Network tended to have more datasets related to financials/budgets than to labor statistics or datasets more traditionally difficult to find.

There's also no way to (usefully) refine a search on **Open Data Network**. I could only choose between "Publishers" or "Catagories", both of which seemed to do nothing to limit my search. 

![Screen Shot](https://github.com/readelev/cj-2016/week-01/sshot1.png) ![Screen Shot 2](cj-2016/week-01/sshot1.png)

##data.cityofpaloalto.org

The **City of Palo Alto** portal was not intuitive to dig through and seemed to be designed for its color scheme rather than for maximum ease of use, BUT I liked how you could do some simple sorts online before downloading the entire dataset. 

Within each dataset, I think more variables could be collected to make the dataset more useful. For example, for Annual Water Consumption, rather than recording just "Year" and "Water (CCF Annual)" the city could record monthly usage or % change, or add columns for population change, permits involved, etc.

I also couldn't find a statistic for total datasets involved.

##Federal Electtion Commission

While the others portals made finding interesting datasets easier, FEC's portal was difficult to sift though without a plan. The layout of the FEC page takes me back to the 90's where I have to scroll through undifferentiated results akin to what a Yahoo search would produce and then fill in bubbles before downloading my data (see images below):
  
![FEC Search Results](https://github.com/readelev/cj-2016/week-01/Screen Shot 2016-03-29 at 4.03.38 PM.png)

I wanted to know more about each dataset and the data collected before being asked to choose a download option. At the same time, I thought the RSS feed option was cool (does this mean you can track updates?)

Other thoughts: the "Maps" tab on the lefthand side seemed a bit useless, and I couldn't find a way to download any geospatial data. Similarly, the "Charts" were too simplified to be useful and didn't do a good job of succincly communicating the takeaways from any particular dataset.

##data.gov.uk

29,375 results.

I liked **data.gov.uk** much better than its American cousin mostly because of the "Additional Information" table at the bottom of each dataset that described (among other things) the date added, geographic regions covered, temporal coverage, and any relevant mandates. I love the site analytics tab (total page views 22,436,334!) with India coming in 3rd by country for % views (at 1.28%, after the UK and US).

I liked that all datasets related to a particular theme, for example, the monthly data for planned road works, were grouped together on the same page with extraneous data (in this case, from 2015 and backwards) minimized and represented only one search result through the main portal.


Trying to get fancy with Markdown, I created a table of XX (below). Portals are ranked on a scale of :persevere: to :kissing_heart:, with :kissing_heart: ranking slightly higher than :grinning:, and so on.

lowest :persevere: :disappointed: :expressionless: :grinning: :kissing_heart: highest

*category* | data.gov | Open Data Network | data.cityofpaloalto | FEC.gov/data | data.gov.uk
---------- | ---------- | ---------- | ---------- | ---------- | ---------- 
Ability to refine search | :expressionless: | :persevere: | :disappointed: | :grinning: | :grinning:
Ease of use |:disappointed: |:grinning: |:expressionless: | :disappointed:| :kissing_heart:
No. datasets | :kissing_heart: | :grinning: | ? | ? | :grinning:
Usefulness of data | :grinning: | :grinning: | :disappointed: | :grinning: | :grinning:
Finding interesting datasets | :disappointed: | :expressionless: | :expressionless: | :disappointed: | :grinning:

#Giancarlo Esposito

Data: http://www.nyc.gov/html/nypd/html/analysis_and_planning/stop_question_and_frisk_report.shtml

Here's the relevant paragraph:
>Days before the interview, Esposito was stopped and frisked by New York police while walking out of a theater 
>where he was rehearsing a play. After several frantic minutes – with him and officers screaming, and their guns 
>drawn – they realized they had the wrong guy. Their suspect had a hoodie, and Esposito was wearing a suit. When 
>it was over, one of the officers recognized him, from his recent turn on ABC's "Once Upon a Time."

I'm not sure how I would do this, mostly because I don't know what each column refers to in the dataset...

BUT I could at least limit by
1. "In/Out" (Esposito was let go)
2. By date, within a couple of days of the interview. 
3. Location (Manhattan) and, presumably, a bit more accurate if I get an address of the theater.

