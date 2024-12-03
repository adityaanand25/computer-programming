# Implement a basic voting system where users can vote for candidates and see the results.

votes = {}
def vote(candidate):
    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1
vote("Alice")
vote("Bob")
vote("Alice")
print("Voting Results:", votes)
