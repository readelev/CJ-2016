# Hey! This is week three.

How are we already so far into the quarter.

![img](http://placekitten.com/800/100)

# Homework

## Due Wednesday, 2016-04-20 23:59

##1. Find the first press briefing in which ISIS or ISIL were mentioned in a White House press briefing

First step is to download all the press briefings from President Obama's presidency (January 2011 to today) and save them as html files. 

[This script](https://github.com/readelev/cj-2016/tree/master/week-03/wh-briefings-word-scrape.py) downloads each page of press briefings and saves them as html files in a folder called "index-pages". 

Then, [my "ALLTOGETHERNOW" script](https://github.com/readelev/cj-2016/tree/master/week-03/wh-briefings-ALLTOGETHERNOW.py):
* Gathers all the index pages
* Gets the text from each and parses the HTML
* Selects for each <a> tag nested within <h3> tags
* Creates a filename from the relative href path

Finally, [this search](https://github.com/readelev/cj-2016/tree/master/week-03/wh-briefings-ISIL-search.py) opens each file and searches for mentions of ISIS or ISIL.

I found the **first mention of ISIS/ISIL was on October 31, 2013** in a [briefing by Press Secretary Jay Carney](https://www.whitehouse.gov/the-press-office/2013/10/31/press-briefing-press-secretary-jay-carney-10312013). Carney mentions ISIL once:


> MR. CARNEY:...we have a very firmly held belief that the foreign military sales program is one of our largest, and is an important symbol of the long-term security partnership between the United States and Iraq, envisioned by both countries.  And we're committed to delivering on foreign military sales equipment that is currently under contract as quickly as possible as part of our effort to address the ongoing terrorist threat.
>
>We have interests at stake here.  We consider the government of Iraq an essential partner in the fight against a common enemy, al Qaeda in Iraq, *which now calls itself the Islamic State of Iraq* and the Levant. Iraqi security forces are confronting an increasingly large, sophisticated and well-armed **ISIL** network, which is able to mount coordinated and complex attacks. 

Because Carney mentioned the "Islamic State of Iraq" before he mentioned the acronym "ISIL", I did a [search for "Islamic State of Iraq"](https://github.com/readelev/cj-2016/tree/master/week-03/wh-briefings-IslamicState-search.py) as well, just to make sure the first mention was on the same date (it was).


##2. Count the number of mentions (including all variations in spelling) of ISIS, ISIL, Osama bin Laden, and Al-Qaeda within the published White House press briefings

##3. List the name of every executed Texas inmate who did not mention religion in their final words: http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html

##4. For the 2015 session of the Supreme Court, list the Supreme Court justices in descending order of number of times they talked, according to the oral transcripts: http://www.supremecourt.gov/oral_arguments/argument_transcript/2015







