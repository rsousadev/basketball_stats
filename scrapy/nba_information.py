from nba_api.stats.static import players, teams


class GetNBAPlayerInformation:
    @staticmethod
    def get_player_by_first_name(firstname: str) -> dict:
        return players.find_players_by_first_name(firstname)

    @staticmethod
    def get_player_by_last_name(lastname: str) -> dict:
        return players.find_players_by_last_name(lastname)

    @staticmethod
    def get_player_by_full_name(fullname: str) -> dict:
        return players.find_players_by_full_name(fullname)


class GetNBATeamInformation:
    @staticmethod
    def get_team_by_full_name(team_name: str) -> dict:
        return teams.find_teams_by_full_name(team_name)

    @staticmethod
    def get_teams_by_state(state: str) -> dict:
        return teams.find_teams_by_full_name(state)

    @staticmethod
    def get_teams_by_city(city: str) -> dict:
        return teams.find_teams_by_city(city)

    @staticmethod
    def get_teams_by_nickname(nick: str) -> dict:
        return teams.find_teams_by_nickname(nick)

    @staticmethod
    def get_teams_by_year_founded(year_founded: str) -> dict:
        return teams.find_teams_by_nickname(year_founded)

    @staticmethod
    def get_all_teams():
        return teams.get_teams()
