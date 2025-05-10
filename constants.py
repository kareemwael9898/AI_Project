# Grid and display settings
GRID_WIDTH, GRID_HEIGHT = 6, 6  
CELL_SIZE = 70  
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE  
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE  

# Control visualization speed (30 FPS)
Frame_RATE = 200  # FPS

# Color definitions (RGB)
WHITE = (255, 255, 255)  # Empty paths
BLACK = (0, 0, 0)        # Walls
RED = (250, 0, 0)        # Agent
# very light yellow
YELLOW = (255, 255, 200)  # Visited cells

GRAY = (180, 180, 180)   # Grid lines
BLUE = (0, 120, 255)     # Goal
GREEN = (0, 200, 0)      # Path visualization