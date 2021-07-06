# Chinasa "Chi-Chi" Iheanacho
matches = ["Match 1", "Match 2", "Match 3", "Match 4", "Match 5"]
team1_scores = [0, 0, 0, 0, 0]
team2_scores = [0, 0, 0, 0, 0]
winner = [0, 0, 0, 0, 0]
TEAM1 = 0
TEAM2 = 0
W2 = ['', '', '', '', '']
for i in range(5):
    team1 = int(input("What did Team One score in Match {}?".format(i + 1)))
    team2 = +int(input("What did Team Two score in Match {}?".format(i + 1)))
    if team1 > team2:
        team1_scores[i] = team1_scores[i] + team1
        team2_scores[i] = team2_scores[i] + team2
        TEAM1 = TEAM1 + 1
        # print(TEAM1)
        W2[i] = W2[i].replace('', 'Team 1')
        # print(W2)
    elif team2 > team1:
        team2_scores[i] = team2_scores[i] + team2
        team1_scores[i] = team1_scores[i] + team1
        TEAM2 = TEAM2 + 1
        # print(TEAM2)
        W2[i] = W2[i].replace('', "Team 2")
        # print(W2)
    else:
        team1_scores[i] = team1_scores[i] + team1
        team2_scores[i] = team2_scores[i] + team2
        winner[i] = winner[i] + 1
        W2[i] = W2[i].replace('', "Tie")
        # print(W2)
print("{:<10}{:<10} {:>5} {:>10}".format("", "Team 1", "Team 2", "Winner"))
for i in range(len(matches)):
    print("{:<10}{:<10} {:>2} {:>14}".format(matches[i], team1_scores[i], team2_scores[i], W2[i]))
if TEAM1 > TEAM2:
    print("The Winner is Team 1.")
elif TEAM2 > TEAM1:
    print("The Winner is Team 2.")
else:
    print("The Tournament is Tied.")







