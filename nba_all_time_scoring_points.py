"""Program Introduction:

   This program is called "The Nba All Time Scoring Points Calculator" utilizes inputs from users and a created data file to calculate an 
   estimate of how many points an NBA player will score by the time they retire"""

import csv

"""utilizing a function called "get_avg_games_per_season" to get the average games per season each NBA player in the data file has played, by:
utilizing a paramater called "player_name", opening up my created csv data file, reading that csv file, splitting the data
in rows so that it can get just the number for the average games per season and the name of the player that the number
is associated to, getting the third element from the list by "[2]" and returning that value and the name of the player"""
def get_avg_games_per_season(player_name):
    file_name = "nba_players_info.csv"
    with open(file_name, newline = '') as file:
        read_csv = csv.reader(file)
        for row in read_csv:
            if row[0].split(',')[0] == player_name:
                avg_games_per_season = float(row[0].split(',')[2])
                return avg_games_per_season
    return None

"""utilizing a function called "get_career_avg_points" to get the career average points for each NBA player in the data file by:
utilizing a parameter called "player_name", opening and reading my created csv data file, splitting the data in rows so that it can just
get the number and player associated with that number, getting the fourth element from the list by "[3]" and returning that value
and the name of the player"""
def get_career_avg_points(player_name):
    file_name = "nba_players_info.csv"
    with open(file_name, newline = '') as file:
        read_csv = csv.reader(file)
        for row in read_csv:
            if row[0].split(',')[0] == player_name:
                career_avg_points = float(row[0].split(',')[3])
                return career_avg_points
    return None

"""utilizing a function called "get_first_season" to get the starting season for each NBA player in the data file by:
utilizing a parameter called "player_name", opening and reading my created csv data file, splitting the data in rows so that it can just
get the number and player associated with that number, getting the fifth element from the list by "[4]" and returning that value
and the name of the player"""
def get_first_season(player_name):
    file_name = "nba_players_info.csv"
    with open(file_name, newline = '') as file:
        read_csv = csv.reader(file)
        for row in read_csv:
            if row[0].split(',')[0] == player_name:
                first_nba_season = float(row[0].split(',')[4])
                return first_nba_season
    return None

"""utilizing a function called "get_info_total_points()" to calculate the total points any NBA player in my csv data file will score
by the user's chosen final NBA season date by: utilizing inputs for users to type in, opening and reading the csv file, printing a list of the players
and their teams, prompting the user to select an NBA player from the given list through input, calling the other three previous functions above, another input
is utilized to ask the user to input a year date they think the NBA player will retire, the function will calculate the total points based on that input, if the
user inputs any invalid data at any point, the function raises a ValueError with a message explaining the error, after the calculations have finished and a total
score is given, the function will continue to prompt the user to chose another player or to end the program if the users wants to"""
def get_info_total_points():
    file_name = "nba_players_info.csv"
    player_dict = {}
    with open(file_name, newline = '') as file:
        read_csv = csv.reader(file)
        print("Select an NBA player from the list below by entering their first and last name:")
        print()
        for row in read_csv:
            player_name = row[0].split(',')[0]
            player_team = row[0].split(',')[1]
            print(f"Player: {player_name}")
            print(f"Team: {player_team}")
            print()
            player_dict[player_name] = player_team

    while True:
        current_player = input("Select an NBA player from the list above by entering their first and last name: ")
        print()

        try:
            avg_games = (get_avg_games_per_season(current_player))
            career_avg = (get_career_avg_points(current_player))
            first_season = (get_first_season(current_player))

            if avg_games is None or career_avg is None or first_season is None:
                raise ValueError("Sorry, the player has not been found. Please check your spelling and the list and try again.")

            avg_games = float(avg_games)
            career_avg = float(career_avg)
            first_season = int(first_season)
            print(f"You have selected {current_player}, who plays for the {player_dict[current_player]}.")
            print()

            final_season_input = input(f"Starting from the 2023 NBA season, enter the season that you think {current_player} will retire (just a four digit year, the year the NBA season ends): ")
            print()

            if not final_season_input.isdigit():
                raise ValueError("Sorry, this input is invalid. Please enter an NBA season that is either the current season or a future season. Start again by selecting an NBA player from the list given.")
            
            final_season = int(final_season_input)

            if final_season < 2024:
                raise ValueError("Sorry, this input is invalid. Please enter an NBA season that is either the current season or a future season. Start again by selecting an NBA player from the list given.")
                
            total_seasons = (final_season - first_season)
            total_points = ((avg_games * career_avg) * total_seasons)
                
            print(f"By the end of the {final_season - 1}-{final_season} NBA season, {current_player} will have scored a total of {int(total_points)} points.")
            print()

            
            end_program = input("Would you like to end the program? Enter 'end' to terminate the program and enter anything else to continue the program: ")
            print()

            if end_program == 'end':
                print("The Program Has Been Ended.")
                break
            else:
                continue
            
        except ValueError as e:
            print(e)
            print()

get_info_total_points()
