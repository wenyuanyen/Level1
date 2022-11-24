if __name__ == '__main__':
    player = ['Ari','Bob','Coco','David','Eva','Freda','Gary','Henry','Iris','Janice']
    injured_players = ['Eva','Henry']
    active_players = [name for name in player if name not in injured_players]

    print(active_players)
