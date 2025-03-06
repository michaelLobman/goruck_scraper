# GORUCK SCRAPER

This is a Python scraper for GORUCK's free workouts, fired off by executing the `run.py` file.

## Features

There are three main classes and associated processes in the scraper, all of which are executed by the `executor` class:
  1. Scraper
  2. Merger
  3. Aggregator

### Scraper

The scraper fetches the workout data from GORUCK's actively updated workout page. It writes the data to `./files/goruck_to_prepend.txt`. While fetching the data, it will retrieve each workout sequentially until it reaches the first workout in `./files/goruck_merged.txt`. This avoids duplicate data from being fetched and written.

Before writing, scraper class will create a backup of the prepend file if it exists.

### Merger

The merger class merges the newly fetched results with the most recent `goruck_merged.txt` file. If the file exists, a backup is created prior to the writing.


### Aggregator

Finally, the Aggregator class filters the full workout list by the inclusion of a single keyword, and, optionally, if a threshold of optional keywords is met. 

Similarly to the Scraper and Merger classes, a backup of the aggregated file is created before writing the filtered data.


## Archival Workouts

More information coming soon...

## Shared Classes

More information coming soon...

## 



# TODO: Add **kwargs** handlings for aggregaotr, create next instance for each argument
# TODO: Refactor merge files method to a shared class?
# TODO: Remove unused imports
