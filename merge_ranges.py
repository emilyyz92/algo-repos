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
    print(combine_meetings(sorted_meetings))

def check_meeting(meetings):
    check = False
    if len(meetings) > 1:
        for (i, meeting) in enumerate(meetings[1:]):
            prev_meet = meetings[i]
            if meeting[0] >= prev_meet[0] and meeting[0] <= prev_meet[1]:
                check = True
                break
    # pdb.set_trace()
    return check


def combine_meetings(meetings):
    if not check_meeting(meetings):
        return meetings
    else:
        combined_meetings = []
        i = 1
        while i < len(meetings):
            prev_meet = meetings[i - 1]
            meeting = meetings[i]
            if meeting[0] >= prev_meet[0] and meeting[0] <= prev_meet[1]:
                if meeting[1] > prev_meet[1]:
                    combined_meetings.append((prev_meet[0], meeting[1]))
                else:
                    combined_meetings.append(prev_meet)
            else:
                combined_meetings.append(prev_meet)
                combined_meetings.append(meeting)
            i += 1
            pdb.set_trace()
        return combine_meetings(list(set(combined_meetings)))

merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])