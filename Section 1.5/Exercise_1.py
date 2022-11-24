if __name__ == '__main__':
    player = {'Ari','Bob','Coco','David','Eva','Freda','Gary','Henry','Iris','Janice'}
    injured_players = {'Eva','Henry'}
    active_players = player.difference(injured_players)

    print(active_players)

    # the benefit is that we don't need to loop through the entire player list

