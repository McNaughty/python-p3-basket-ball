def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }

game_dictionary = game_dict()
# name="Kristaps Porzingis"

def player_details(game_dictionary):
    # empty list that will hold all players combined
    all_players = []
    # game_dictionary.items() iterates over the key-value pairs in the game_dictionary. 
    # each key is a team type ("home" or "away")
    # value is a dictionary containing details about that team.
    for team_type, team_details in game_dictionary.items():
        # extracts the list of players for the current team.
        players = team_details.get("players", [])
        all_players.extend(players)
    return all_players



def num_points_per_game(player_name):
    players_details = player_details(game_dictionary)
    for player in players_details:
        if player["name"] == player_name:
                return player.get("points_per_game")
    return None

def player_age(player_name):
    players_details = player_details(game_dictionary)
    for player in players_details:
        if player["name"] == player_name:
            return player.get("age")
    return None

def team_colors(team_name):
    if isinstance(game_dictionary, dict):
        for team_type, team_details in game_dictionary.items():
            if team_details["team_name"] == team_name:
                colors = team_details.get("colors", [])
                print(f"{team_name} team colors: {colors}")
                return colors
        return []


def team_names():
    teams = []
    for team_type, team_details in game_dictionary.items():
        teams.append(team_details["team_name"])
    return teams

def player_numbers(team):
    jersey_numbers = []
    for team_type, team_details in game_dictionary.items():
        if team_details["team_name"] == team:
            for player in team_details["players"]:
                number = player["number"]
                jersey_numbers.append(number)
    return jersey_numbers
        

def player_stats(name):
    # player_stats_list = []
    for team_type, team_details in game_dictionary.items():
        for player in team_details["players"]:
            if player["name"] == name:
                return {
                    "name": player["name"],
                    "number": player["number"],
                    "position": player["position"],
                    "points_per_game": player["points_per_game"],
                    "rebounds_per_game": player["rebounds_per_game"],
                    "assists_per_game": player["assists_per_game"],
                    "steals_per_game": player["steals_per_game"],
                    "blocks_per_game": player["blocks_per_game"],
                    "career_points": player["career_points"],
                    "age": player["age"],
                    "height_inches": player["height_inches"],
                    "shoe_brand": player["shoe_brand"]
                }
    return {}

def average_rebounds_by_shoe_brand():
    # Create a dictionary to store rebounds for each shoe brand
    shoe_brand_rebounds = {}

    # Iterate through teams and players in the game dictionary
    for team_type, team_details in game_dictionary.items():
        for player in team_details["players"]:
            shoe_brand = player["shoe_brand"]
            rebounds = player["rebounds_per_game"]

            # Update the shoe brand rebounds dictionary
            if shoe_brand not in shoe_brand_rebounds:
                shoe_brand_rebounds[shoe_brand] = [rebounds]
            else:
                shoe_brand_rebounds[shoe_brand].append(rebounds)

    # Calculate the average rebounds for each shoe brand
    average_rebounds_dict = {}
    for brand, rebounds_list in shoe_brand_rebounds.items():
        average_rebounds = sum(rebounds_list) / len(rebounds_list)
        average_rebounds_dict[brand] = average_rebounds

    # Print the result with adjusted formatting
    for brand, average_rebounds in average_rebounds_dict.items():
        print(f"{brand}:  {average_rebounds:.2f}")

average_rebounds_by_shoe_brand()

