# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
     #initializare stiva (fiecare element este un tuplu(stare,actiune_pana_la_stare)
     # care retine starile pe care le explorez
    stack = util.Stack()

    #initializare set gol de vizite ce va retine starile pe care le-am vizitat
    visited = set()

    #stare initiala a labirintului
    start_state = problem.getStartState()

    #adaugarea in lista a starii initaile si lista goala de actiuni
    stack.push((start_state, []))  

    #bucla DFS, ruleaza pana cand stiva este goala
    while not stack.isEmpty(): 
        #extrage starea curenta si actiunea asociata din vf stivei
        current_state, actions = stack.pop() 

        if current_state in visited:
            continue #omitem starile deja vizitate

        #verif. daca starea curenta este obiectivul
        # daca da se returneaza lsita de actiuni care a dus la acea stare
        if problem.isGoalState(current_state):
            return actions
        
        #daca starea curenta nu a fost deja vizitata
        if current_state not in visited:
            visited.add(current_state)  # Adăugăm starea curentă în mulțimea de stări vizitate

        successors = problem.getSuccessors(current_state)  # Obținem successori

    # Parcurgem fiecare successor și adăugăm pe stivă
        for successor, action, _ in successors:
            new_actions = actions + [action]  # Actualizăm lista de acțiuni cu noua acțiune
            stack.push((successor, new_actions))  # Adăugăm successorul împreună cu noile acțiuni pe stivă

    # Dacă nu s-a găsit o soluție, returnăm o listă goală
    return []

    #util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    
     #initializare coada de perechi(stare,actiune_pana_la_stare)
     # care retine starile pe care le explorez
    queue = util.Queue()

    #initializare set gol de vizite ce va retine starile pe care le-am vizitat
    visited = set()


    #stare initiala a labirintului
    start_state = problem.getStartState()

    #adaugarea in lista a starii initaile si lista goala de actiuni
    queue.push((start_state, []))  

    #bucla BFS, ruleaza pana cand coada este goala
    while not queue.isEmpty(): 
        #extrage starea curenta si actiunea asociata din vf cozii
        current_state, actions = queue.pop() 

        if current_state in visited:
            continue #omitem starile deja vizitate

        #verif. daca starea curenta este obiectivul
        # daca da se returneaza lsita de actiuni care a dus la acea stare
        if problem.isGoalState(current_state):
            return actions
        
        #daca starea curenta nu a fost deja vizitata
        if current_state not in visited:
            visited.add(current_state)  # Adăugăm starea curentă în mulțimea de stări vizitate


        successors = problem.getSuccessors(current_state)  # Obținem successori

         # Parcurgem fiecare successor și adăugăm in coada
        for successor, action, _ in successors:
            new_actions = actions + [action]  # Actualizăm lista de acțiuni cu noua acțiune
            queue.push((successor, new_actions))  
            # Adăugăm successorul împreună cu noile acțiuni pe coada

    # Dacă nu s-a găsit o soluție, returnăm o listă goală
    return []
    #util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    #initializare coada de prioritati(tuplu(stare,actiune_pana_la_stare, costul_total_pana_acum)
    # care retine starile pe care le explorez
    priority_queue = util.PriorityQueue()

    #initializare set gol de vizite ce va retine starile pe care le-am vizitat
    visited = set()

    #stare initiala a labirintului
    start_state = problem.getStartState()

    #adaugarea in lista a starii initaile si lista goala de actiuni
    priority_queue.push((start_state, [],0),0 +0)  

    #bucla UCS, ruleaza pana cand coada este goala
    while not priority_queue.isEmpty(): 
        #extrage starea curenta,actiunile si costul total pana la staredin fata cozii
        current_state, actions, total_cost = priority_queue.pop() 

        if current_state in visited:
            continue #omitem starile deja vizitate

        #verif. daca starea curenta este obiectivul
        # daca da se returneaza lsita de actiuni care a dus la acea stare
        if problem.isGoalState(current_state):
            return actions
        
        #daca starea curenta nu a fost deja vizitata
        if current_state not in visited:
            visited.add(current_state)  
            # Adăugăm starea curentă în mulțimea de stări vizitate

        successors = problem.getSuccessors(current_state)  # Obținem successori

    # Parcurgem fiecare successor și adăugăm in coada
        for successor, action, step_cost in successors:
            new_actions = actions + [action]  # Actualizăm lista de acțiuni cu noua acțiune
            new_cost = total_cost + step_cost # Calculam noul cost total

            priority_queue.push((successor, new_actions,new_cost),new_cost)  
            # Adăugăm successorul împreună cu noile acțiuni si noul cost total in coada

    # Dacă nu s-a găsit o soluție, returnăm o listă goală
    return []
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    #initializare coada de prioritati(tuplu(stare,actiune_pana_la_stare, costul_total_pana_acum)
    # care retine starile pe care le explorez
    priority_queue = util.PriorityQueue()

    #stare initiala a labirintului
    start_state = problem.getStartState()

    #initializare set gol de vizite ce va retine starile pe care le-am vizitat
    visited = set()

    #adaugarea in lista a starii initaile, costul asociat, lista goala de actiuni si euristica
    priority_queue.push((start_state, [], 0), 0 + 0+ heuristic(start_state,problem))

    #bucla A*, ruleaza pana cand coada este goala
    while not priority_queue.isEmpty():

        #extrage starea curenta,actiunile si costul asociat pana la stare din fata cozii
        current_state, actions, cost = priority_queue.pop()

        if current_state in visited:
            continue #omitem starile deja vizitate

        #verif. daca starea curenta este obiectivul
        # daca da se returneaza lsita de actiuni care a dus la acea stare
        if problem.isGoalState(current_state):
            return actions

        # Adăugăm starea curentă în mulțimea de stări vizitate
        visited.add(current_state)
        
        # Obținem successori
        successors = problem.getSuccessors(current_state)

        #Parcurgem fiecare successor și adăugăm in coada
        for successor, action, step_cost in successors:
            new_actions = actions + [action]
            new_cost = cost + step_cost

            priority_queue.push((successor, new_actions, new_cost), new_cost + heuristic(successor, problem))
             # Adăugăm successorul împreună cu noile acțiuni si noul cost total in coada + euristica
    return []
    #util.raiseNotDefined()
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
