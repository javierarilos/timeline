
def from_csv(csv_filename, separator=';', skip_first=True):
    """parse an event_list from a CSV file
    """
    event_list = []
    with open(csv_filename, 'r') as csv_file:
        if skip_first:
            csv_file.readline()
        for csv_line in csv_file.readlines():
            splitted = csv_line[:-1].split(separator)
            event_list.append(splitted)
    return event_list
