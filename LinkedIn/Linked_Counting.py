
import collections
def countGoogle(arr):
    return min(collections.Counter(arr).items(), key=lambda x:x[1])[0]