import urllib.request, json, http.client

team_url = 'teams'
fixture_url = 'fixtures'
token = '3fb170b312d34191a5be1fbf76292f11'
league_id = input('Which league would you like to see? (398 = Premier league)')

def connect(key, url):
    """Function to connect to football data api

    Retrieves latest data from football data api and returns it. Accepts an API
    token and part of the URL to determine which data to return (both
    strings)"""

    connection = http.client.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': key, 'X-Response-Control': 'minified' }
    connection.request('GET', '/alpha/soccerseasons/' + league_id + '/' + url, None, headers )
    return json.loads(connection.getresponse().read().decode())

league_data = connect(token, team_url)
fixtures = connect(token, fixture_url)

class Team:
    """Class to store team data from selected league

    name, abbreviation (strings) and value (int) are stored"""
    def __init__(self, name, abbr, value):
        if type(name) != str or type(abbr) != str:
            raise TypeError('The name and abbreviation must be strings')
        if type(value) != int:
            raise TypeError('The value must be an integer')
        self.name = name
        self.abbr = abbr
        self.value = value

class Fixture:
    """Holds info on league fixtures

    Contains fixture information of every game of the season"""
    def __init__(self, home_team, away_team, home_team_score, away_team_score):
        if type(home_team) != str or type(away_team) != str:
            raise TypeError('The teams were not of the correct type(string)')

        elif type(home_team_score) != int or type(away_team_score) != int:
            raise TypeError('The score must be an integer value')

        if home_team_score < -1 or away_team_score < -1:
            raise ValueError('A team cannot score negative goals (although United could certainly give it a try...)')

        self.home_team = home_team
        self.away_team = away_team
        self.home_team_score = home_team_score
        self.away_team_score = away_team_score

obj_list = []
for i in range(len(league_data['teams'])):
    i = Team(
        league_data['teams'][i]['name'],
        league_data['teams'][i]['shortName'],
        int(league_data['teams'][i]['squadMarketValue'][:-1]
            .replace(',','')))
    obj_list.append(i)

fixture_list = []
for i in range(len(fixtures['fixtures']) - 1):
    if fixtures['fixtures'][i]['status'] == 'FINISHED':
        #Produces full list of completed fixtures
        """
        print(
                fixtures['fixtures'][i]['homeTeamName'] + ' ' + 
                str(fixtures['fixtures'][i]['result']['goalsHomeTeam']) + ' vs ' +
                fixtures['fixtures'][i]['awayTeamName'] + ' ' +
                str(fixtures['fixtures'][i]['result']['goalsAwayTeam'])
                )
                """
        i = Fixture(
                fixtures['fixtures'][i]['homeTeamName'],
                fixtures['fixtures'][i]['awayTeamName'],
                fixtures['fixtures'][i]['result']['goalsHomeTeam'],
                fixtures['fixtures'][i]['result']['goalsAwayTeam'])
        fixture_list.append(i)

def createTable(teams, fixtures):
    """Produces up to date league table

    Analyses both classes and creates an up to date version of the league table
    accounting for goal difference, as well as producing a list of clubs sorted
    by market value for comparison"""

    d = {}
    points_for_win = 3
    table = []
    for i in range(len(teams)):
        #set equal to a tuple (points, goal difference)
        d[teams[i].name] = (0, 0)

    for i in range(len(fixtures)):
    #Manages changes in points and goal difference
        home = fixtures[i].home_team
        away = fixtures[i].away_team
        home_goals = fixtures[i].home_team_score
        away_goals = fixtures[i].away_team_score
        home_points, home_goal_difference = d[home] 
        away_points, away_goal_difference = d[away]

        if home_goals > away_goals:
            tmp_goal_difference = home_goals - away_goals
            d[home] = (home_points + points_for_win, tmp_goal_difference + home_goal_difference)
            d[away] = (away_points, away_goal_difference + (tmp_goal_difference
                * -1))
        elif home_goals < away_goals:
            tmp_goal_difference = away_goals - home_goals
            d[away] = (away_points + points_for_win, away_goal_difference +
                tmp_goal_difference)
            d[home] = (home_points, home_goal_difference + (tmp_goal_difference * -1))
        else:
            d[home] = (home_points + 1, home_goal_difference)
            d[away] = (away_points + 1, away_goal_difference)

    for i in range(len(teams)):
        #Produce full table
        name = teams[i].name
        points, gd = d[teams[i].name]
        value = teams[i].value
        table.append((teams[i].name, points, gd, value))
    
    #Sort table
    sorted_table = (sorted(table, key=lambda tup: (tup[1], tup[2])))
    sorted_table.reverse()
    value_table = sorted(table, key=lambda tup: (tup[3]))
    value_table.reverse()

    #Display table
    print('Team  |  Points  |  Goal Difference  | Value(€) | Teams ordered by value')
    for i in range(len(teams)):
        if i == len(teams) - 3:
            print('-' * 70)
        name, points, gd, value = sorted_table[i]
        #b, c, val1 are not needed, just to prevent unpacking overload
        name_by_value, b, c, val = value_table[i]
        remainder_spaces = 25 - len(name)
        if len(str(gd)) == 2:
            gd_spaces = 2
        elif len(str(gd)) == 1:
            gd_spaces = 3
        elif len(str(gd)) == 3:
            gd_spaces = 1
        if len(str(points)) == 1:
            points_spaces = 2
        else:
            points_spaces = 1
        print(name + (' ' * remainder_spaces) + ' | ' + str(points) + ' ' *
        points_spaces + '|' + ' ' + str(gd) + ' ' * gd_spaces + '| ' + str(value) + ' | ' + 
        name_by_value)
    return d

createTable(obj_list, fixture_list)
