
from collections import defaultdict
from datetime import datetime

def load_cheaters(cheaters_file):
   """
    Load the cheaters from the file and return a set of cheaters

    arguments: 
    cheaters_file: path to the file containing the cheaters

    returns:
    cheaters: a set of cheaters"""
   
   cheaters = set()
   with open(cheaters_file, 'r') as f:
       for line in f:
           cheater_id = line.split('\t')[0]
           cheaters.add(cheater_id)
   return cheaters

def load_team_data(team_file):
   """
   Loads team data from the given file

   arguments:
    team_file: path to the file containing the team data

   returns:
   team_dict (dict): a dictionary mapping match id and team_id to a list of player IDs
   match_team_player (list): a list of tuples containing match_id, team_id, and account_id"""

   team_dict = defaultdict(list) # Map team_id to a list of player IDs
   match_team_player = []  
   with open(team_file, 'r') as f:
       for line in f:
           match_id, account_id, team_id = line.strip().split('\t')
           team_dict[(match_id, team_id)].append(account_id)
           match_team_player.append((match_id, team_id, account_id))
   return team_dict, match_team_player


def parse_cheaters(cheaters):
    """
   Parse cheaters data and return a dictionary

   arguments:
    cheaters: path to the file containing the cheaters file

   returns:
   cheaters_group: a dictionary with player_id as key and a tuple of cheat_start and ban_date as value"""
    
    cheaters_group = {}
    with open(cheaters, 'r') as f:
        for line in f:
            # Extract player ID, cheat start date, and ban date
            player_id, cheat_start, ban_date = line.strip().split('\t')
            # Map the player ID to their cheat start and ban dates
            cheaters_group[player_id] = (cheat_start, ban_date)
    return cheaters_group

def parse_kills(killing):
    """
    parse the killing data and return a list of tuples
    
    arguments:
    killing: path to the file containing the killing data

    returns:
    kills: a list of tuples containing match_id, killer_id, victim_id, and kill_dt
    """
    kills = []
    with open(killing, 'r') as f:
        for line in f:
            # Extract match ID, killer ID, victim ID, and kill time
            match_id, killer_id, victim_id, kill_time = line.strip().split('\t')
            # Convert the kill time to a datetime object
            kill_dt = datetime.strptime(kill_time, '%Y-%m-%d %H:%M:%S.%f')
            kills.append((match_id, killer_id, victim_id, kill_dt))
    return kills

def get_match_start_times_from_kills(kills):
    """
    determine the start time of each match based on the first kill in the match
    
    arguments:
    kills: a list of tuples containing match_id, killer_id, victim_id, and kill_dt
    
    returns:
    match_start_times: a dictionary mapping match_id to the start time of the match
    """
    match_start_times = {}

    for match_id, killer_id, victim_id, kill_dt in kills:
        # If the match ID is new or this kill occurred earlier than the recorded time
        if match_id not in match_start_times or kill_dt < match_start_times[match_id]:
            match_start_times[match_id] = kill_dt # Update the match start time

    return match_start_times

def group_kills_by_match(kills):
    """
    group kills by match_id
    
    arguments:
    kills: a list of tuples containing match_id, killer_id, victim_id, and kill_dt
    
    returns:
    match_groups: a dictionary mapping match_id to a list of tuples containing killer_id, victim_id, and kill_dt
    """
    match_groups = {}

    # Loop through all kill events
    for match_id, killer_id, victim_id, kill_time in kills:
        if match_id not in match_groups:
            match_groups[match_id] = []
            # Append the event to the appropriate match group
        match_groups[match_id].append((killer_id, victim_id, kill_time))
    return match_groups
