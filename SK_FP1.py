
def bruteForceMiceToHole(micepositions, holepositions):
    timetaken = set()
    holetaken = set()
    for i, mice in enumerate(micepositions):
        time = {}
        for j, hole in enumerate(holepositions):
            difference = abs(mice - hole)
            time[difference] = j
        time = sorted(time.items())
        for diff, index in time:
           if not holepositions[index] in holetaken:
              timetaken.add(diff)
              holetaken.add(holepositions[index])
              break
    return max(timetaken)


              
    
def greedyMiceToHole(micepositions, holepositions):
    micepositions.sort()
    holepositions.sort()
    time = 0
    for i, mice in enumerate(micepositions):
        difference = abs(micepositions[i] - holepositions[i])
        time = max(time, difference)
    return time


mice = [4, -4, 2]
hole = [4, 0, 5]
resultBruteForce = bruteForceMiceToHole(mice, hole)
resultGreedy = greedyMiceToHole(mice, hole)

print(f"max time from brute = {resultBruteForce}, greedy = {resultGreedy}")
