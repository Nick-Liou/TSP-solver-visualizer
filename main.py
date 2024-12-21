
# Import necessary libraries
import tsplib95
import networkx as nx
import matplotlib.pyplot as plt
import random
import math

import file_paths



# --- PART A: Parsing TSPLIB Files ---
def parse_tsplib_file(file_path :str ) -> None:
    """
    Parse a TSPLIB file and print its details.

    Parameters:
        file_path (str): Path to the TSPLIB file.
    """
    try:
        problem = tsplib95.load(file_path)
        print("Problem Name:", problem.name)
        print("Problem Type:", problem.type)
        print("Number of Nodes:", problem.dimension)
        print("Edge Weight Type:", problem.edge_weight_type)

        # Optionally, write to an output file
        with open("output.txt", "w") as output_file:
            output_file.write(f"Problem Name: {problem.name}\n")
            output_file.write(f"Problem Type: {problem.type}\n")
            output_file.write(f"Number of Nodes: {problem.dimension}\n")
            output_file.write(f"Edge Weight Type: {problem.edge_weight_type}\n")
    except Exception as e:
        print("Error parsing TSPLIB file:", e)

    

# --- MAIN EXECUTION ---
def main() -> None:
    
     # Example usage

    # PART A: Parse a TSPLIB file
    file_path = "your_tsplib_file.tsp"  # Replace with the actual file path

    file_path = file_paths.select_file()
    print(file_path)
    
    parse_tsplib_file(file_path)

    # Create a simple TSP graph for demonstration
    G = nx.complete_graph(5)
    for (u, v) in G.edges():
        G[u][v]['weight'] = random.randint(1, 100)  # Assign random weights

    # # PART B: Solve TSP using heuristics
    # nn_tour = nearest_neighbor_heuristic(G)
    # sa_tour = simulated_annealing_heuristic(G)

    # print("Nearest Neighbor Tour:", nn_tour)
    # print("Simulated Annealing Tour:", sa_tour)

    # # PART C: Visualize the tours
    # print("Visualizing Nearest Neighbor Tour")
    # visualize_tour(G, nn_tour)

    # print("Visualizing Simulated Annealing Tour")
    # visualize_tour(G, sa_tour)


if __name__ == "__main__":

    main()

