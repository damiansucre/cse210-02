from game.card import Card


class Game_action:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.dice = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        #for i in range(5):
        card = Card()
        self.dice.append(card)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        values = 0
        card = self.dice
        values = f"{card.value} "
        print(f"the card is: {values}")

        roll_dice = input("play again? [y/n] ")
        self.is_playing = (roll_dice == "y")
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        for i in range(len(self.dice)):
            card = self.dice[i]
            card.roll()
            self.score += card.points 
        self.total_score += self.score

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.dice)):
            card = self.dice[i]
            values += f"{card.value} "

        print(f"You rolled: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)
