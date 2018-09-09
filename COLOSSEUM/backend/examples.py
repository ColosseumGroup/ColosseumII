DEBUG_MATCH_INFO_EXAMPLE = {
    'gameID': '10112323123',  # just ID number
    'game': 'dealer_poker',  # name of the game
    'NPC': 'starter',  # 'False' 'starter' 'master' 'Godlike'
    'rounds': '100',
    'random_seed': '0',  # 'False' 'int'
    'game_define': 'holdem.limit.2p.reverse_blinds.game',  # for poker game define file is required
    't_response':'6000000',  # maximum time per response in milliseconds
    't_hand': '600000',  # maximum player time per hand in milliseconds
    't_per_hand':'70000',  # maximum average player time for match in milliseconds
    'wait_time_out':'1000000', # maximum time to wait for players to connect in milliseconds
    'keep_transaction':'True', # True if keep the transaction file to rebuild the game
    'fixed_ports': {
        'if_fixed':'True',  # Random ports if False
        'ports':[
            {'port_1':'12345'},
            {'port_2':'23456'}
            ]   # port number if 'if_fixed' is True
    },  # try to start a game with given ports by users
    'players': [
        {'name_1': 'Alice'},
        {'name_2': 'Bob'}
    ]
}


REFEREE_RET_EXAMPLE = {
    'status': 'success',  # Task.STATUS  and   'game no exist'
    'score': 'SCORE:47|53:a|b'  # False if game is no success
}

KILL_PROCESS_CONTROL_EXAMPLE = {
    'gameID':'12312',
    'action':'terminate'  # 'terminate' 'startTime'(check process start time) 'status' (process current status)
}


RESULT = {
    'status': 'ongoing',
    'score': 'False',
    'xxx': 12312
}