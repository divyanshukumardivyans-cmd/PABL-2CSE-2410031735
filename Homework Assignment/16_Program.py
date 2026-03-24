#Given an array of intervals where intervals[i] = [starti, endi], merge alloverlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # Overlapping intervals
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)

    return merged

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals))