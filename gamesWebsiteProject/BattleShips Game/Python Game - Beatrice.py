import random

GRID_SIZE = 10
MAX_TURNS = 10

# Ships and their sizes
ships = {
    'Destroyer': 2,
    'Submarine': 3,
    'Battleship': 4
}

def random_row():
    return random.randint(0, GRID_SIZE - 1)

def random_col():
    return random.randint(0, GRID_SIZE - 1)

def place_ship(ship, size, grid):
    """Randomly place a single ship on the grid."""
    while True:
        row = random_row()
        col = random_col()
        is_vertical = random.choice([True, False])

        # Vertical placement
        if is_vertical:
            if row + size > GRID_SIZE:
                continue
            # Check if space is free
            if any(grid[row + i][col] != '.' for i in range(size)):
                continue
            # Place ship
            for i in range(size):
                grid[row + i][col] = ship[0]

        # Horizontal placement
        else:
            if col + size > GRID_SIZE:
                continue
            if any(grid[row][col + i] != '.' for i in range(size)):
                continue
            for i in range(size):
                grid[row][col + i] = ship[0]
        break
    return True

def place_ships(grid):
    """Place all ships on the grid."""
    for ship, size in ships.items():
        place_ship(ship, size, grid)
    return grid

def fire(row, col, grid):
    """Handle firing at a cell and return the result."""
    mark = grid[row][col]
    if mark == 'X' or mark == '-':
        print("\nYou've already fired at this location. Try somewhere new!")
        return None
    elif mark != '.':
        print(f"\n \U0001F4A5 Hit! {mark} ship segment destroyed.")
        grid[row][col] = 'X'
        return mark
    else:
        print("\n \U0001F30A You missed!")
        grid[row][col] = '-'
        return False

def print_grid(grid, fog_of_war=True):
    """Print the grid. Fog hides enemy ships."""
    print('   ' + ' '.join(map(str, range(GRID_SIZE))))
    for i, row in enumerate(grid):
        if fog_of_war:
            row_display = [
                'X' if cell == 'X' else
                '-' if cell == '-' else
                '.' for cell in row
            ]
        else:
            row_display = row
        print(f'{i:2} ' + ' '.join(row_display))

def print_help():
    print("\U0001F6A2 \U0001F6A2 \U0001F6A2  Welcome to Battleship! \U0001F6A2 \U0001F6A2 \U0001F6A2")
    print("Enter row and column numbers (0–9) to fire at that square.")
    print("You have 10 turns to sink all enemy ships.")
    print("X = hit, - = miss")
    print("Good luck!\n")

def main():
    print_help()

    # Player grid (for your ships)
    player_grid = [['.'] * GRID_SIZE for _ in range(GRID_SIZE)]
    player_grid = place_ships(player_grid)

    # Enemy grid (hidden)
    enemy_grid = [['.'] * GRID_SIZE for _ in range(GRID_SIZE)]
    enemy_grid = place_ships(enemy_grid)

    print("\nDEBUG: Enemy grid (for testing):")
    print_grid(enemy_grid, fog_of_war=False)

    # DEBUG – reveal enemy grid if needed
    # print("\nDEBUG: Enemy Grid (no fog):")
    # print_grid(enemy_grid, fog_of_war=False)

    ships_remaining = len(ships)
    turns = 0

    while ships_remaining > 0 and turns < MAX_TURNS:
        turns += 1
        print(f"\n--- Turn {turns}/{MAX_TURNS} ---")
        print("(Type 'quit' to exit the game)")

        action = input("Enter row and column (e.g. '3 5'): ").strip()
        if action.lower() == 'quit':
            print("\nYou chose to quit the game.")
            return

        coordinates = action.split()
        if len(coordinates) != 2:
            print("\nInvalid input. Please enter two numbers (row col).")
            continue

        try:
            row, col = map(int, coordinates)
            if not (0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE):
                print("\nInvalid coordinates. Try again.")
                continue
        except ValueError:
            print("\nInvalid input. Please use numbers only.")
            continue

        hit_ship = fire(row, col, enemy_grid)

        # If hit, check if the ship is fully destroyed
        if hit_ship:
            ship_name = [name for name, size in ships.items() if name[0] == hit_ship][0]
            # Flatten grid to see if ship still exists
            if hit_ship not in ''.join(''.join(r) for r in enemy_grid):
                print(f"\n \U0001F525 You destroyed the enemy's {ship_name}!")
                ships_remaining -= 1

        # Display grids
        print("\nYour Grid:")
        print_grid(player_grid, fog_of_war=False)
        print("\nEnemy Grid:")
        print_grid(enemy_grid)

    # End of game
    if ships_remaining == 0:
        print("\n \U0001F389 All enemy ships destroyed! You win!")
    elif turns >= MAX_TURNS:
        print("\n \U0001F480 Out of turns! Game over.")
    else:
        print("\n \U0001F44F Game ended.")

if __name__ == "__main__":
    main()