# GORUCK SCRAPER

This is a Python scraper for GORUCK's free workouts, fired off by executing the `run.py` file.

## Classes

There are three main classes and associated processes in the scraper, all of which are executed by the `executor` class:
  1. Scraper
  2. Merger
  3. Aggregator

### Executor

Instatiates with instances of Scraper, Merger, and Converter classes as properties. All three processes can be run by evoking `execute_all`, though each process can be fired off individually as well, e.g. `execute_scraper`.

### Scraper

The scraper fetches the workout data from GORUCK's actively updated workout page. It writes the data to `./files/goruck_to_prepend.txt`. While fetching the data, it will retrieve each workout sequentially until it reaches the first workout in `./files/goruck_merged.txt`. This avoids duplicate data from being fetched and written.

Before writing, scraper class will create a backup of the prepend file if it exists.

### Merger

The Merger class merges the newly fetched results with the most recent `goruck_merged.txt` file. If the file exists, a backup is created prior to the writing.


### Converter

The Converter class initializes a dataframe from the `goruck_merged.txt` file, flattening the various formats into a rigid structure. I am currently building this out to handle all workout formats.


#### TODOS

  1. buy in, cash out, notes, scoring, amrap, etc
  2. format to csv
  3. front end with datatables for filtering
  4. clean up code to be less nested and more pythonic
