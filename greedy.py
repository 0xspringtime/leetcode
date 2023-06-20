def activitySelection(activities):
    # Sort the activities by their finish time
    activities.sort(key = lambda x: x[1])
    
    # The first activity is always selected
    selected_activities = [activities[0]]
    last_finish_time = activities[0][1]

    # For the rest of the activities
    for activity in activities[1:]:
        # If the activity starts after the last one finishes, select it
        if activity[0] >= last_finish_time:
            selected_activities.append(activity)
            last_finish_time = activity[1]
            
    return selected_activities

# Time complexity: O(n log n) because of the sort operation.
# Space complexity: O(n) for the list of selected activities.

#Define the problem constraints and the objective to optimize.
#
#Identify if this problem can be solved by making a greedy choice, meaning that a local optimum will lead to a global optimum.
#
#Sort or organize your data if necessary. Greedy algorithms often deal with sorted data or use priority queues.
#
#Make the greedy choice. Often this involves a loop that iterates over the input and at each step makes the decision that looks the best at the moment.
#
#Lastly, prove that the solution is correct and analyze its time and space complexity.
