# [pychronic](https://pypi.org/project/pychronic/)
## Introduction
A natural language date parser in Python. Inspired from Ruby's chronic.

## Installation
`pip install pychronic`

### Usage:
* Datetime To Natural Langauge
```
 from pychronic.utils import to_natural_time
 from datetime import datetime, timedelta, date

>>> to_natural_time(datetime.now())
{'day': 'today', 'time': '10:56 PM', 'month': 'September', 'year': 2019, 'day_of_week': 'Friday'}

>>> to_natural_time(datetime.now() - timedelta(days=1))
{'day': 'yesterday', 'time': '10:56 PM', 'month': 'September', 'year': 2019, 'day_of_week': 'Thursday'}

>>> to_natural_time(datetime.now() + timedelta(days=1))            
{'day': 'tomorrow', 'time': '10:57 PM', 'month': 'September', 'year': 2019, 'day_of_week': 'Saturday'}

>>> to_natural_time(datetime(year=2019, month=1, day=1, hour=1, minute=0, second=0))
{'day': '1st', 'time': '01:00 AM', 'month': 'January', 'year': 2019, 'day_of_week': 'Tuesday'}
```

* Highlight datetime in text

```
from pychronic.utils import highlight_from_text

>>> highlight_from_text("Tournament will commence on 12:30 PM on 23rd May and end on 25th aug")
{'input': ['Tournament', 'will', 'commence', 'on', '12:30', 'PM', 'on', '23rd', 'May', 'and', 'end', 'on', '25th', 'aug'], 'matched_pattern': [{'from_index': 4, 'to_index': 8, 'parsed_value': datetime.datetime(2019, 5, 23, 12, 30)}, {'fro
m_index': 12, 'to_index': 13, 'parsed_value': datetime.date(2019, 8, 25)}]}

>>> highlight_from_text("Tournament will commence on 11:30 PM on 23rd May and end on 25th aug")
{'input': ['Tournament', 'will', 'commence', 'on', '11:30', 'PM', 'on', '23rd', 'May', 'and', 'end', 'on', '25th', 'aug'], 'matched_pattern': [{'from_index': 4, 'to_index': 8, 'parsed_value': datetime.datetime(2019, 5, 23, 23, 30)}, {'fro
m_index': 12, 'to_index': 13, 'parsed_value': datetime.date(2019, 8, 25)}]}

>>> highlight_from_text("Today is 25th of december")
{'input': ['Today', 'is', '25th', 'of', 'december'], 'matched_pattern': [{'from_index': 2, 'to_index': 4, 'parsed_value': datetime.date(2019, 12, 25)}]}

>>> highlight_from_text("Results are on 23-may-2019 or 24-may-2019")
{'input': ['Results', 'are', 'on', '23-may-2019', 'or', '24-may-2019'], 'matched_pattern': [{'from_index': 3, 'to_index': 3, 'parsed_value': datetime.date(2019, 5, 23)}, {'from_index': 5, 'to_index': 5, 'parsed_value': datetime.date(2019,
 5, 24)}]}

```

### Contributing
Fork and pull request.

### Contributors
[Jayesh](https://github.com/jayeshathila.com)


## Stats
![visitors](https://visitor-badge.glitch.me/badge?page_id=jayeshathila.Pychronic)	![code-size](https://img.shields.io/github/languages/code-size/jayeshathila/Pychronic)