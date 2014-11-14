def average(vals):
    " calculate the median of vals "
    return sum(vals)/float(len(vals))

def median(entries):
    " return the middle value from a set of sortable entries "
    return sorted(entries)[len(entries)/2]
