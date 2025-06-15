from simulation import Simulation
# Run the simulation
if __name__ == "__main__":
# we will play 100000 times, and in each simulation we will play 15 games how many times we will win, something like bernoulli with law of large numbers
    counter = 0
    for_for= 100000
    games =15
    for i in range(for_for):
        simulation = Simulation(games, display=False)
        if simulation.run():
            counter += 1
    print(f"Winning probability whith switching when we played {games} games: {counter / for_for:.4f} ({counter} wins out of {for_for}simulations)")


    # probability of winning in 1 games, with law of large numbers
    simulation = Simulation(100000, display=True)
    simulation.run()