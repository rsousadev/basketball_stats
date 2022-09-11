from requests import get

from basketball_reference_scraper.box_scores import get_box_scores
from basketball_reference_scraper.injury_report import get_injury_report
from basketball_reference_scraper.pbp import get_pbp
from basketball_reference_scraper.players import (
    get_game_logs,
    get_player_headshot,
    get_stats,
)
from basketball_reference_scraper.seasons import get_schedule, get_standings
from basketball_reference_scraper.shot_charts import get_shot_chart
from basketball_reference_scraper.teams import (
    get_opp_stats,
    get_roster,
    get_roster_stats,
    get_team_misc,
    get_team_stats,
)
from nba_information import GetNBAPlayerInformation


class GetPlayerInformation:
    def __init__(self):
        self.get_nba_infos = GetNBAPlayerInformation()

    @staticmethod
    def get_players_by_team_year(nick: str, year: int) -> dict:
        players = get_roster(nick, year)
        return players.to_dict()

    @staticmethod
    def get_players_stats_by_team_year(
        nick: str, year: int, data_format: str = "PER_GAME", playoffs: bool = False
    ) -> dict:
        player_stats = get_roster_stats(nick, year, data_format, playoffs)
        return player_stats.to_dict()

    @staticmethod
    def get_players_stats_by_name(
        name: str,
        stat_type: str = "PER_GAME",
        playoffs: bool = False,
        career: bool = False,
    ) -> dict:
        player_stats = get_stats(name, stat_type, playoffs, career)
        return player_stats.to_dict()

    @staticmethod
    def get_players_stats_by_name_year(
        name: str,
        year: int,
        playoffs: bool = False,
    ) -> dict:
        player_stats = get_game_logs(name, year, playoffs)
        return player_stats.to_dict()

    def get_player_headshot(self, name: str) -> dict:
        player_info = self.get_nba_infos.get_player_by_full_name(name)
        player_headshot = " The Player Headashot Not Found"
        if player_info:
            player_id = player_info[0]["id"]
            request_player = get(f"https://www.nba.com/stats/player/{player_id}/career")

            if request_player.status_code == 200:
                player_headshot = (
                    f"https://cdn.nba.com/headshots/nba/latest/1040x760/{player_id}.png"
                )
        return {"url_image": player_headshot}
