import pygame
from constants import *
from environment import MazeEnv
from q_learning import train_q_learning
from visualization import run_visualization, setup_environment

show_training_visualization = True

def draw_button(screen, text, rect, color_normal, color_hover, mouse_pos):
    """
    Draw a button on the screen with hover effect.
    """
    if rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, color_hover, rect)
    else:
        pygame.draw.rect(screen, color_normal, rect)
    
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def main_menu():
    """
    Display the main menu and handle user input.
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Maze Q-Learning")

    global show_training_visualization

    running = True
    while running:
        # Fill the screen color
        screen.fill(YELLOW)
        mouse_pos = pygame.mouse.get_pos()

        # Display the maze size
        maze_size = f"Current Maze Size: {GRID_WIDTH} x {GRID_HEIGHT}" 
        font = pygame.font.Font(None, 36)
        text_surface = font.render(maze_size, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(400, 100))
        screen.blit(text_surface, text_rect)

        draw_button(screen, "Random Maze", pygame.Rect(300, 200, 200, 50), (0, 128, 0), (0, 255, 0), mouse_pos)
        draw_button(screen, "Manual Maze", pygame.Rect(300, 300, 200, 50), (0, 128, 0), (0, 255, 0), mouse_pos)
        draw_button(screen, "Exit", pygame.Rect(300, 400, 200, 50), (128, 0, 0), (255, 0, 0), mouse_pos)

        # #####################################################
        checkbox_text = "Show Visualization" if show_training_visualization else "Hide Visualization"
        checkbox_font = pygame.font.Font(None, 24)
        checkbox_text_surface = checkbox_font.render(checkbox_text, True, (0, 0, 0))
        checkbox_text_rect = checkbox_text_surface.get_rect(center=(400, 500))
        screen.blit(checkbox_text_surface, checkbox_text_rect)

        # Draw CheckBox for boolean value to show or hide visualization
        checkbox_rect = pygame.Rect(300, 490, 20, 20)
        pygame.draw.rect(screen, (255,255,255), checkbox_rect, 2)

        # change value of checkbox_state when clicked
        if pygame.mouse.get_pressed()[0]:
            if checkbox_text_rect.collidepoint(mouse_pos) or checkbox_rect.collidepoint(mouse_pos):
                show_training_visualization = not show_training_visualization
                
                # Wait for the next click to change the state
                while pygame.mouse.get_pressed()[0]:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            break

        if show_training_visualization == True:
            pygame.draw.rect(screen, (0, 255, 0), checkbox_rect)
        else:
            pygame.draw.rect(screen, (255, 0, 0), checkbox_rect)
        # #####################################################

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click
                    if pygame.Rect(300, 200, 200, 50).collidepoint(mouse_pos):
                        return 'random'
                    elif pygame.Rect(300, 300, 200, 50).collidepoint(mouse_pos):
                        return 'manual'
                    elif pygame.Rect(300, 400, 200, 50).collidepoint(mouse_pos):
                        return None

        pygame.display.flip()

    pygame.quit()
    return None

def main():
    choice = main_menu()
    print(f"User choice: {choice}")
    if choice == 'random':
        env = MazeEnv(mode='random')
        print("\nRandom maze generated automatically.")
        setup_environment(env)
    elif choice == 'manual':
        env = MazeEnv(mode='manual')
        print("\nManual maze setup mode activated.")
        print("Left-click to add walls, right-click to remove walls.")
        print("Press ENTER to start training once done.\n")
        setup_environment(env)
    elif choice is None:
        print("Exiting the program.")
        return
    
    print("Training Q-learning agent...")
    if show_training_visualization:
        print("Visualization enabled.")
        q_table = train_q_learning(env, episodes=200, epsilon_decay=0.99, min_epsilon=0.01, with_visualization=True)
    else:
        print("Visualization disabled.")
        q_table = train_q_learning(env, episodes=200, epsilon_decay=0.99, min_epsilon=0.01, with_visualization=False)
    print("Training completed.")

    print("Running visualization...")
    run_visualization(env, q_table)

if __name__ == "__main__":
    main()