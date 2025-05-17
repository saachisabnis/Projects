from collections import defaultdict
import random

def count_cheaters_in_teams(team_dict, cheaters):
   """
   Count the number of cheaters in each team

   arguments:
   team_dict: a dictionary mapping (match_id, team_id) to a list of player IDs
   cheaters: a set of cheaters

   returns:
   cheater_counts: a list of the number of cheaters in each team
   """
   cheater_counts = [] 
   for (match_id, team_id), players in team_dict.items():
       #count the number of cheaters in each team
       num_cheaters = sum(1 for player in players if player in cheaters)
       #ensure that cheater_counts is long enough to store the number of cheaters in each team
       while len(cheater_counts) <= num_cheaters:
           cheater_counts.append(0)
        #increment the count of teams with this number of cheaters
       cheater_counts[num_cheaters] += 1
   return cheater_counts



def actual_counts(cheaters, team_dict):
  """
   Calculate and display the actual counts of teams with varying numbers of cheaters.
   
   arguments:
    cheaters (set): A set of player IDs representing cheaters.
    team_dict (dict): A dictionary where keys are tuples of (match_id, team_id) and  values are lists of player IDs in each team.

    returns:
    list: A list where the index represents the number of cheaters in a team, and the value at that index is the number of teams with that many cheaters.
    
    """
  cheater_counts = count_cheaters_in_teams(team_dict, cheaters)
  print("Actual counts:")
  for num_cheaters, count in enumerate(cheater_counts):
      print(f"Teams with {num_cheaters} cheaters: {count}")
  return cheater_counts





def shuffle_team_within_match(match_team_player, number_of_shuffles=20):
    """
    Shuffle team IDs within each match, keeping players in the same match but reassigning team IDs.

    arguments:
    match_team_player: list of tuples containing match_id, team_id, and account_id
    number_of_shuffles: int, number of times to shuffle team IDs within each match

    returns:
    shuffled_teams: a dictionary mapping (match_id, team_id) to a list of player IDs (shuffled)
    """
    shuffled_teams = defaultdict(list) #to store shuffled teams compositions
    match_grouped = defaultdict(list) #to group players by match
    
    # Group players by match
    for match_id, team_id, player_id in match_team_player:
        match_grouped[match_id].append((team_id, player_id))
    
    # Shuffle team IDs within each match
    for match_id, entries in match_grouped.items():
        team_ids = [entry[0] for entry in entries] #extracting team IDs
        players = [entry[1] for entry in entries] #extracting player IDs
        random.shuffle(team_ids)

        # Re-assign players to shuffled team IDs
        for team_id, player_id in zip(team_ids, players):
            shuffled_teams[(match_id, team_id)].append(player_id)

    return shuffled_teams

def randomised_cheater_counts(match_team_player, cheaters, number_of_shuffles=20):
    """
    Perform multiple shuffles of team IDs within each match and count the number of cheaters in each team.

    arguments:
    match_team_player: list of tuples containing match_id, team_id, and account_id
    cheaters: set of cheaters
    number_of_shuffles: int, number of times to shuffle team IDs within each match

    returns:
    aggregate_cheater_counts: list of tuples containing the number of cheaters in each team for each shuffle
    """
    shuffled_cheater_counts= []
    #performing shuffling and counting cheaters for each shuffle
    for _ in range(number_of_shuffles):
        shuffled_dict = shuffle_team_within_match(match_team_player)
        cheaters_counts = count_cheaters_in_teams(shuffled_dict, cheaters)
        # Append the counts as a tuple to the list of shuffled results
        shuffled_cheater_counts.append(tuple(cheaters_counts))
    # Transpose the shuffled results to aggregate counts across all shuffles
    # Each tuple in the result corresponds to the counts for a specific number of cheaters in teams
    aggregate_cheater_counts = [tuple(group) for group in zip(*shuffled_cheater_counts)]
    return aggregate_cheater_counts