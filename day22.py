def stories(story_durations, total_time):

     story_durations.sort()
     # [5, 10, 15, 20, 30]

     res = 0
     count = 0 

     for i in range(len(story_durations)):
          if res + story_durations[i] <= total_time:
              res += story_durations[i]
              count += 1
          else:
              break

     return count


story_durations = [10, 15, 20, 5, 30]
total_time = 50

print(stories(story_durations, total_time))