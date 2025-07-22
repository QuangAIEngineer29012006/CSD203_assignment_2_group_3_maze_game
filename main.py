import system

def main():
    user_input = input(
        "Choose algorithm (1–4):\n"
        "1. Prim\n"
        "2. Kruskal\n"
        "3. Recursive (DFS)\n> "
        "4. BFS\n"
        "Enter your choice: "
    )
    size = int(input("Enter maze size (10 < size < 50): "))
    if size > 10 and size < 200:
        if user_input == '1': 
            system.start_game(ALGORITHM='prim', MAZE_SIZE=size)
        elif user_input == '2':
            system.start_game(ALGORITHM='kruskal', MAZE_SIZE=size)
        elif user_input == '3':
            system.start_game(ALGORITHM='dfs', MAZE_SIZE=size)
        elif user_input == '4':
            system.start_game(ALGORITHM='bfs', MAZE_SIZE=size)
        else:
            print("Invalid input. Choose a number from 1 to 4.")    

if __name__ == "__main__":
    main()