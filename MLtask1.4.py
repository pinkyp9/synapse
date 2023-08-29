import random as r 

class ChessPlayer:
    def __init__(self, name, age, ELO, tenacity, isBoring):
        self.name = name
        self.age = age
        self.ELO = ELO
        self.tenacity = tenacity
        self.isBoring = isBoring
        self.tournament_score = 0

def simulateMatch(player1, player2):
    elo_difference = abs(player1.ELO - player2.ELO)
    if (((player1.isBoring==True and player2.isBoring==False)or(player2.isBoring==True and player1.isBoring==False)) and (elo_difference<100)):
        player1.tournament_score += 0.5
        player2.tournament_score += 0.5
    elif elo_difference > 100:
        if player1.ELO > player2.ELO:
            player1.tournament_score += 1
        else:
            player2.tournament_score += 1
    elif elo_difference <= 100 and elo_difference > 50:
        random_factor = r.randint(1, 10)
        if player1.ELO < player2.ELO:
            lplayer = player1
            hplayer = player2
        else:
            lplayer = player2
            hplayer = player1
        lower_elo_multiplier = random_factor * lplayer.tenacity
        if lower_elo_multiplier > hplayer.ELO:
            lplayer.tournament_score += 1
        else:
            hplayer.tournament_score += 1
    else:
        if player1.tenacity > player2.tenacity:
            player1.tournament_score += 1
        else:
            player2.tournament_score += 1
    #print(player1.name ,"score :",player1.tournament_score)
    #print(player2.name ,"score :",player2.tournament_score)

players = [
    ChessPlayer("Courage the Cowardly Dog", 25, 1000.39, 1000, False),
    ChessPlayer("Princess Peach", 23, 945.65, 50, True),
    ChessPlayer("Walter White", 50, 1650.73, 750, False),
    ChessPlayer("Rory Gilmore", 16, 1700.87, 500, False),
    ChessPlayer("Anthony Fantano", 37, 1400.45, 400, True),
    ChessPlayer("Beth Harmon", 20, 2500.34, 150, False)
]

for i in range(len(players)):
    for j in range(i + 1, len(players)):
        print('player:'+ players[i].name +'and'+ players[j].name )
        simulateMatch(players[i], players[j])
        simulateMatch(players[j], players[i])


for player in players:
    print(player.name,':', player.tournament_score ,'points')
