import urllib.request, json, http.client

team_url = 'teams'
fixture_url = 'fixtures'
token = '3fb170b312d34191a5be1fbf76292f11'

def connect(key, url):
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': key, 'X-Response-Control': 'minified' }
    connection.request('GET', '/alpha/soccerseasons/398/' + url, None, headers )
    return json.loads(connection.getresponse().read().decode())

league_data = connect(token, team_url)
fixtures = connect(token, fixture_url)

print(fixtures)

class Team:
    def __init__(self, name, abbr, value):
        if type(name) != str or type(abbr) != str:
            raise TypeError('The name and abbreviation must be strings')
        if type(value) != int:
            raise TypeError('The value must be an integer')
        self.name = name
        self.abbr = abbr
        self.value = value

class Fixture:
    def __init__(self, home_team, away_team, home_team_score, away_team_score):
        if type(home_team) != str or type(away_team) != str:
            raise TypeError('The teams were not of the correct type(string)')

        elif type(home_team_score) != int or type(away_team_score) != int:
            raise TypeError('The score must be an integer value')

        if home_team_score < -1 or away_team_score < -1:
            raise ValueError('A team cannot score negative goals')

        self.home_team = home_team
        self.away_team = away_team
        self.home_team_score = home_team_score
        self.away_team_score = away_team_score

obj_list = []
for i in range(len(league_data['teams']) - 1):
    i = Team(
        league_data['teams'][i]['name'],
        league_data['teams'][i]['shortName'],
        int(league_data['teams'][i]['squadMarketValue'][:-1]
            .replace(',','')))
    obj_list.append(i)

fixture_list = []
print(fixtures['fixtures'][0]['result']['goalsAwayTeam'])
for i in range(len(fixtures['fixtures']) - 1):
    if fixtures['fixtures'][i]['status'] == 'FINISHED':
        print(
                fixtures['fixtures'][i]['homeTeamName'] + ' ' + 
                str(fixtures['fixtures'][i]['result']['goalsHomeTeam']) + ' vs ' +
                fixtures['fixtures'][i]['awayTeamName'] + ' ' +
                str(fixtures['fixtures'][i]['result']['goalsAwayTeam'])
                )
        i = Fixture(
                fixtures['fixtures'][i]['homeTeamName'],
                fixtures['fixtures'][i]['awayTeamName'],
                fixtures['fixtures'][i]['result']['goalsHomeTeam'],
                fixtures['fixtures'][i]['result']['goalsAwayTeam'])
        fixture_list.append(i)

def createTable( teams, fixtures ):
    d = {}
    print(len(teams))
    for i in range(len(teams) - 1):
        #set equal to a tuple (points, goal difference)
        d[teams[i].name] = (0, 0)

    print(len(fixtures))

    for i in range(len(fixtures) - 1):
        home = fixtures[i].home_team

        for i in range(len(obj_list) - 1):
            if home == teams[i].name:
                points, goal_difference = d[teams[i].name]

        away = fixtures[i].away_team
        home_score = fixtures[i].home_team_score
        away_score = fixtures[i].away_team_score
        print(home_score)
        print(away_score)
        home_goal_difference = home_score - away_score
        away_goal_difference = away_score - home_score
        if home_score > away_score:
            print('Home win')
            d[home] = (points + 3, goal_difference + home_goal_difference)
        elif home_score == away_score:
            print('Draw')
            d[home] = (points + 1, goal_difference)
            d[away] = (points + 1, goal_difference)
        else:
            #print('Away win')
            d[away] = (points + 3, goal_difference + away_goal_difference)
    return d

#print(createTable(obj_list, fixture_list))
createTable(obj_list, fixture_list)
