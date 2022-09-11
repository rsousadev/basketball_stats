from nba_api.stats.static import players

# Find players by full name.
players.find_players_by_full_name("james")

# Find players by first name.
players.find_players_by_first_name("lebron")

# Find players by last name.
players.find_players_by_last_name("^(james|love)$")

# Get all players.
players.get_players()
