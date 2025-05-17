from datetime import datetime
import random
from data_processing import *



def is_cheating(killer, match_start_time, cheaters):
    """
    checks if a player was cheating at a given time
    
    arguments:
    killer: str, player ID of the killer
    match_start_time: datetime object, the start time of the match
    cheaters: dict, a dictionary with player_id as key and a tuple of cheat_start and ban_date as value
    
    returns:
    bool: True if the player was cheating at the given time, False otherwise
    """
    if killer not in cheaters:
        return False  # Player not in cheaters list
    cheat_start, _ = cheaters[killer]
    cheat_start_dt = datetime.strptime(cheat_start, '%Y-%m-%d')
    return match_start_time >= cheat_start_dt

def does_victim_become_cheater(victim, match_start_time, cheaters):
    """
    check if a player became a cheater after being killed
    
    arguments:
    victim: str, player ID of the victim
    match_start_time: datetime object, the start time of the match
    cheaters: dict, a dictionary with player_id as key and a tuple of cheat_start and ban_date as value
    
    returns:
    bool: True if the player became a cheater after being killed, False otherwise"""
    if victim not in cheaters:
        return False  # victim is not in the cheaters list
    cheat_start, _ = cheaters[victim]
    cheat_start_dt = datetime.strptime(cheat_start, '%Y-%m-%d')
    # Check if the cheat start date is after the match start time
    return cheat_start_dt > match_start_time

def count_true_conditions(kills, cheaters, match_start_times):
    """
    count the number of situations where victims of cheating players become cheaters
    
    arguments:
    kills: list of tuples, each containing match_id, killer, victim, and kill_dt
    cheaters: dict, a dictionary with player_id as key and a tuple of cheat_start and ban_date as value
    match_start_times: dict, a dictionary with match_id as key and start time as value
    
    returns:
    count: int, the number of situations where victims of cheating players become cheaters"""

    count = 0
    for match_id, killer, victim, kill_dt in kills:
        # Check both conditions for cheating
        if is_cheating(killer, match_start_times[match_id], cheaters) and does_victim_become_cheater(victim, match_start_times[match_id], cheaters):
            count += 1
    return count

def randomise_kills_within_match(kills, number_of_shuffles=20):
    """
    Randomise player IDs within each match, while preserving the match structure

    arguments:
    kills: list of tuples containing match_id, killer_id, victim_id, and kill_time
    number_of_shuffles: int, number of times to shuffle player IDs within each match

    returns:
    randomised_kills: list of randomised kill events of tuples containing match_id, killer_id, victim_id, and kill_time
    """
    randomised_kills = []
    match_groups = group_kills_by_match(kills)

    # Shuffle killers and victims within each match
    for match_id, kill_list in match_groups.items():
    
        random_killers = [entry[0] for entry in kill_list]
        random_victims = [entry[1] for entry in kill_list]
        
        random.shuffle(random_killers)
        random.shuffle(random_victims)

        # Ensure no self-kills
        for i in range(len(kill_list)):
            random_killer = random_killers[i]
            random_victim = random_victims[i]
            kill_time = kill_list[i][2]

            # Keep shuffling random_victims until random_killer != random_victim
            while random_killer == random_victim:
                random.shuffle(random_victims)
                random_victim = random_victims[i]

            # Add the randomized kill to the results
            randomised_kills.append((match_id, random_killer, random_victim, kill_time))

    return randomised_kills


def simulate_victim_cheating_events(number_of_randomisations, kills, cheaters):
    """
    Simulate and count victim-to-cheater scenarios over randomisations.

    arguments:
    number_of_randomisations: int, the number of randomisations to perform
    kills: list of tuples containing match_id, killer_id, victim_id, and kill_time
    cheaters: dict, a dictionary with player_id as key and a tuple of cheat_start and ban_date as value

    returns:
    victims_start_cheating_counts: list of counts of victim starting to cheat
    stored_randomisations: list of randomised kills for each randomisation
    """
    stored_randomisations = []
    victims_start_cheating_counts = []
    for _ in range(number_of_randomisations):
        randomised_kills = randomise_kills_within_match(kills) #randomise kills
        stored_randomisations.append(randomised_kills) #save the randomisation
        match_start_times = get_match_start_times_from_kills(randomised_kills) #calculate match start times
        count= count_true_conditions(randomised_kills, cheaters, match_start_times) #count the number of victims starting to cheat
        victims_start_cheating_counts.append(count)
    return victims_start_cheating_counts, stored_randomisations


def get_observers_become_cheaters(kills, cheaters, match_start_times):
    """
    count observers who become cheaters after observing a player kill at least 3 times
    
    arguments:
    kills: list of tuples containing match_id, killer_id, victim_id, and kill_time
    cheaters: dict, a dictionary with player_id as key and a tuple of cheat_start and ban_date as value
    match_start_times: dict, a dictionary with match_id as key and start time as value
    
    returns:
    len(observers): int, the number of observers who become cheaters after observing a player kill at least 3 times"""

    observers = set()

    match_groups = group_kills_by_match(kills) #group kills by match
    for match_id, kills in match_groups.items():
        player_kills = {} #store the number of kills for each player
        earliest_time = datetime.max #initialize the earliest time to the maximum possible time

        for killer_id, victim_id, kill_time in kills:
            # Initialize kill count for the killer
            if is_cheating(killer_id, match_start_times[match_id], cheaters) == False:  # Killer is cheating
                continue
            
            # Initialize or increment the killer's kill count
            if killer_id not in player_kills:
                player_kills[killer_id] = 0
            player_kills[killer_id] += 1

             # Check if the killer meets the condition of having at least 3 kills
            if (
                player_kills[killer_id] >= 3  
            ):
                 # Update the earliest kill time for this match
                if kill_time < earliest_time:
                    earliest_time = kill_time

                # Loop through the kills again to identify valid observers
                for killer_id, victim_id, kill_time in kills:
                    if earliest_time < kill_time and does_victim_become_cheater(victim_id, match_start_times[match_id] , cheaters):
                        observers.add(victim_id)

    return len(observers) # Return the total count of observers who started cheating



def simulate_observer_cheating_events(stored_randomisations, cheaters, match_start_time):
    """simulate and count observer-to-cheater scenarios over randomisations.
    
    arguments:
    stored_randomisations: list of randomised kills for each randomisation
    cheaters: dict, a dictionary with player_id as key and a tuple of cheat_start and ban_date as value
    match_start_time: dict, a dictionary with match_id as key and start time as value
    
    returns:
    observer_cheating_counts: list of counts of observers starting to cheat"""

    observer_cheating_counts = []
     # Loop through each randomization and count observer-to-cheater scenarios
    for randomised_kills in stored_randomisations:
        observers = get_observers_become_cheaters(randomised_kills, cheaters, match_start_time)
        observer_cheating_counts.append(observers)
    return observer_cheating_counts
