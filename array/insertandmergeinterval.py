#insert and merge the interval in the given array

def insert_and_merge(intervals, new_interval):
    merged = []
    i = 0
    n = len(intervals)

    # Add all intervals that come before the new interval
    while i < n and intervals[i][1] < new_interval[0]:
        merged.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    merged.append(new_interval)

    # Add all remaining intervals
    while i < n:
        merged.append(intervals[i])
        i += 1

    return merged

if __name__ == "__main__":
    intervals = []
    n = int(input("Enter the number of intervals: "))
    for _ in range(n):
        interval = list(map(int, input("Enter the interval (start end): ").split()))
        intervals.append(interval)
    new_interval = list(map(int, input("Enter the new interval (start end): ").split()))
    result = insert_and_merge(intervals, new_interval)
    print("Merged intervals:", result)
    