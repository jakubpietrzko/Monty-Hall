from simulation import Simulation

def bernoulli_simulation(trials, games):
    """
    Simulates a Bernoulli process for a given number of trials and games.
    Returns the number of wins.
    """
    counter = 0
    for _ in range(trials):
        simulation = Simulation(games, display=False)
        if simulation.run():
            counter += 1
    return counter
# Run the simulation
if __name__ == "__main__":
# we will play 100000 times, and in each simulation we will play 15 games how many times we will win, something like bernoulli with law of large numbers
    bernoulli = bernoulli_simulation(100000, 15)
    print(f"Number of wins in 100000 trials with 15 games each: {bernoulli}")
    # probability of winning in 1 games, with law of large numbers
    simulation = Simulation(100000, display=True)
    simulation.run()
