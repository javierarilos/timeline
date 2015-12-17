# timeline
Timeline calls your code back following a given time distribution (a planning).
The planning can be easily imported from different formats (eg. from a CSV with timestamps).

## planning
A planning is a list in the form:
```python
[
    [datetime1, arg2, arg3, arg4...],
    [datetime2, arg2, arg3, arg4...],
    ...
]
```

* **planning.start(a_planning)** replays the events by calling a callback     in the same time sequence starting now.
* **planning.is_valid(a_planning)** validates a given planning
* **planning.from_parse_datetimes** converts a list of lists to a planning by parsing a given column to a datetime which is added to first column.


## sample usage

```python
from timeline import planning

a_timeline = [
    ['2015-10-22 13:15:20', 'donald', 'mickey', 'supper together', 'hi there, how about tonight?'],
    ['2015-10-22 13:15:21', 'mickey', 'pluto', 'party', 'hi there, how about tonight?'],
    ['2015-10-22 13:15:22', 'daisy', 'minnie', 'brunch?', 'hi there, how about tonight?'],
    ['2015-10-22 13:15:22', 'donald', 'daisy', 'drinks?', 'hi there, how about tonight?'],
    ['2015-10-22 13:15:22', 'pluto', 'goofy', 'going to the movies', 'hi there, how about tonight'],
    ['2015-10-22 13:15:23', 'donald', 'minnie', 'important update', 'hi there, how about tonight?'],
    ['2015-10-22 13:15:23', 'donald', 'goofy', 'football on sunday', 'hi there, how about tonight'],
    ['2015-10-22 13:15:24', 'goofy', 'micky', 'TIMELINErestriction', 'ts must be sorted, old 2 new']
]
plan = planning.from_parse_datetimes('%Y-%m-%d %H:%M:%S', 0, a_timeline)
planning.is_valid(plan)


def my_cb(a, b, c, d, e):
    print('a:', a, 'b:', b, 'c:', c, 'd:', d, 'e:', e)

planning.start(plan, my_cb)
```
