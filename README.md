﻿# Past, current and upcoming 4G schedule scraped from judu.lt using selenium 

This script fetches all 4G schedules from www.judu.lt, filters them based on the current day and time, and outputs the relevant results to the console. In cases where there are duplicate minutes in the schedule, the script logs these occurrences to a JSON file.

With this script, checking the 4G schedule becomes quick and effortless. It provides a convenient way to access the information you need, tailored to your specific requirements. Whether for personal or professional use, this tool simplifies the process of staying up-to-date with 4G schedules, ensuring you never miss your bus home!


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt

```bash
pip install -r requirements.txt
```

## Usage
Just run with console or open and run in IDE.

You can change outputting logs with console:
```bash
python ./main.py *wanted_log_level*
```

or change it manually in default_log_level.py 
```
DEFAULT = "info"
```
You can choose between debug, info, error and critical levels.
