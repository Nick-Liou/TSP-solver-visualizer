
# Import necessary libraries
from typing import Any
import tsplib95
import networkx as nx
import matplotlib.pyplot as plt

import file_paths



# --- PART A: Parsing TSPLIB Files ---
def parse_tsplib_file(file_path :str ) -> tsplib95.models.Problem:
    """
    Parse a TSPLIB file and return a tsplib95.models.Problem object.

    Parameters:
        file_path (str): Path to the TSPLIB file.
    """
    try:
        problem = tsplib95.load(file_path)
        print("Problem Name:", problem.name)
        print("Problem Type:", problem.type)
        print("Number of Nodes:", problem.dimension)
        print("Edge Weight Type:", problem.edge_weight_type)

        return problem
    
        # # Optionally, write to an output file
        # with open("output.txt", "w") as output_file:
        #     output_file.write(f"Problem Name: {problem.name}\n")
        #     output_file.write(f"Problem Type: {problem.type}\n")
        #     output_file.write(f"Number of Nodes: {problem.dimension}\n")
        #     output_file.write(f"Edge Weight Type: {problem.edge_weight_type}\n")
    except Exception as e:
        print("Error parsing TSPLIB file:", e)



# --- PART C: Visualization ---
def visualize_tour(G: nx.Graph, tour: list[int]) -> None:
    """
    Visualize the TSP tour on a 2D plot.

    Parameters:
        graph (nx.Graph): A NetworkX graph representing the TSP instance.
        tour (list): The TSP tour (list of nodes in visiting order).
    """

    pos = nx.spring_layout(G, weight='weight' ) #, seed=42)
    
    tour_edge_list = list(nx.utils.pairwise(tour))
    # Draw the graph with custom aesthetics
    nx.draw(G,
            pos, 
        with_labels=True,              # Display node labels
        connectionstyle='arc3,rad=0.1' # Curve the edges slightly to reduce overlap
        )


    # Draw the route
    nx.draw_networkx(
        G,
        pos,
        with_labels=True,
        edgelist=tour_edge_list,
        edge_color="red",
        node_size=200,        
        width=3        
    )

    # Display the graph    
    plt.show()




# --- MAIN EXECUTION ---
def main() -> None:
    
    # Example usage

    # PART A: Parse a TSPLIB file
    file_path = "Example_problems/bayg29.tsp"  # Replace with the actual file path

    file_path = file_paths.select_file(file_types=[("TSP files" , "*.tsp"),("ATSP files" , "*.atsp")] , initial_dir= "/Example_problems")

    problem = parse_tsplib_file(file_path)

    # Create the graph from the parsed problem
    G = nx.Graph()
    nodes = list(problem.get_nodes())
    edges = list(problem.get_edges())

    for node in nodes:
        G.add_node(node)

    for edge in edges:
        weight = problem.get_weight(*edge)
        G.add_edge(edge[0], edge[1], weight=weight)


    # PART B: Solve TSP using heuristics
    nn_tour = nx.approximation.greedy_tsp(G)
    print("Nearest Neighbor Tour:", nn_tour)

    sa_tour = nx.approximation.simulated_annealing_tsp(G, "greedy")
    print("Simulated Annealing Tour:", sa_tour)
    

    # PART C: Visualize the tours
    print("Visualizing Nearest Neighbor Tour")
    visualize_tour(G,nn_tour)

    print("Visualizing Simulated Annealing Tour")
    visualize_tour(G,sa_tour)


if __name__ == "__main__":

    main()

