def tournamentWinner(competitions, results):
    # T: O(n) where n is the length of the competitions array
    # M: O(k) where k is the number of unique teams
    scores = {}

    for i, teamNames in enumerate(competitions):
        result = results[i]
        home, away = teamNames

        if result == 1:
            #if home team wins
            if home not in scores:
                scores[home] = 3
            else:
                scores[home] += 3
        else:
            #if away team wins
            if away not in scores:
                scores[away] = 3
            else:    
                scores[away] += 3
        
    return max(scores, key=scores.get)
