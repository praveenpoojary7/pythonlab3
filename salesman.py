#design an application for drilling an optimal printed circuit board . To drill two holes of different diameters consecutively, the head of the machine has to move to a toolbox and change the drilling equipment. this is quite time consuming. Thus it is clear that one has to choose some diameter, drill all holes of same diameter, change the drill, drill holes of the next diameter, etc. Thu this drilling problem has to minimize the travel time for the machine head. Find the optimal time to drill the circuit board.
import networkx as nx
def get_distances(num_nodes):
    distances={}
    for i in range(1,num_nodes+1):
        for j in range(i+1,num_nodes+1):
            distance=float(input(f"Enter the distances between node {i} and node {j}: "))
            distances[(i,j)]=distance
            distances[(j,i)]=distance
    return distances
def tsp_optimal_drilling(distances):
    G=nx.Graph()
    G.add_weighted_edges_from((i,j,distances)for(i,j),distance in distances.items())
    return nx.approximation.traveling_salesman_problem(G,cycle=True)
    #return optimal_order
def calculate_optimal_cost(drill_order,distances):
    total_cost=sum(distances[(drill_order[i],drill_order[i+1])]for i in range(len(drill_order)-1))
    return total_cost
if __name__=="__main__":
    while True:
        num_nodes=int(input("Enter the no of drill holes (nodes): "))
        distances=get_distances(num_nodes)
        optimal_order=tsp_optimal_drilling(distances)
        optimal_cost=calculate_optimal_cost(optimal_order,distances)
        print("Optimal drilling order: ",optimal_order)
        print("Optimal cost: ",optimal_cost)
        t=input("Do you wish to run program from the beginning? (PRESS 1): ")
        if t!=1:
            break
