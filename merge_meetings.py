import pdb

def merge_ranges(meetings):
    #find meeting start times that are after another meeting's start time
    # but before another meeting's end time
    #find meeting with same start time
    #find meetings whose end time is another meeting's start time
    #sort tuples in the meetings list
    sorted_meetings = meetings[:]
    # sort meetings by start time
    sorted_meetings.sort(key = lambda x: x[0])
    return combine_meetings(sorted_meetings)

def combine_meetings(meetings):
    if len(meetings) == 1:
        return meetings
    else:
        i = 0
        while i < len(meetings) - 1:
                if meetings[i+1][0] >= meetings[i][0] and meetings[i+1][0] <= meetings[i][1]:
                    if meetings[i+1][1] > meetings[i][1]:
                        meetings[i] = (meetings[i][0], meetings[i+1][1])
                    del meetings[i+1]
                else:
                    i += 1
        return meetings

print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))