from modules.robotron import Game
import settings


def main():
    # Instancing the game
    robotron = Game(settings.SIZE)

    # Displaying the start game
    robotron.start_screen()
    robotron.new_game()


if __name__ == "__main__":
    main()
