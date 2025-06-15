import random 

from room import Room


# Class that runs the Monty Hall simulation
class Simulation:
    def __init__(self, num_trials, display=True):
        self.success_with_switch = 0
        self.num_trials = num_trials
        self.display = display
    
    def run(self):
        # Runs the simulation for the given number of trials
        for i in range(self.num_trials):
            room = Room()
            player_choice = random.randint(0, 2)
            opened_door = room.open_goat_door(player_choice)
            remaining_door = [i for i in range(3) if i != player_choice and i != opened_door][0]
            
            if room.choose_door(remaining_door).content == "car":
                self.success_with_switch += 1
            
        #    if (i + 1) % 10000 == 0:
        #        self.display_results(i + 1)
        if self.display:
            self.display_results(self.num_trials, final=True)
        if self.success_with_switch / self.num_trials > 0.5:
            return  True
        return False
    def display_results(self, current_trials, final=False):
        # Displays the current or final simulation results
        probability = self.success_with_switch / current_trials
        if final:
            print(f"\nFinal results after {current_trials} trials:")
        else:
            print(f"After {current_trials} trials:")
        print(f"Winning probability when switching: {probability:.4f} ({self.success_with_switch} wins)")
