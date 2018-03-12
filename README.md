get_naics is a web scraper designed to get NAICS codes at no cost by searching businesses in a specific area. This info will be used to generate reports, mainly maps, to report on a city's industrial clusters and to generate reports to attract new businesses. NAICS code format is as follows:

- The first two digits designate the economic sector,
- the third digit designates the subsector, 
- the fourth digit designates the industry group,
- the fifth digit designates the NAICS industry, 
- and the sixth digit designates the national industry

Cleaning up addresses:
- Success rate is only around 40%
- Small businesses are often unlisted
- Major international businesses show up as NOT FOUND since the regex finds businesses by zip code near Madison Heights, MI: (48\d{3})
- siccode.com does not like: dashes (-), "inc", "llc", or "co"
- replace dashes (-) with space
- I haven't found a better NAICS code lookup site