def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    count = 0
    for period in permanence_period:
        if not all(isinstance(i, int) for i in period):
            return None
        if period[0] <= target_time <= period[1]:
            count += 1
    return count
