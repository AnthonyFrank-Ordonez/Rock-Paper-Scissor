import time
from random import choice
from data_files.game_settings import game_template, win, lose,  choices_selection, system_exit


class RSM:
    def __init__(self, selections, user_score: int = 0, ai_score: int = 0, ):
        """Dunder __init__ method"""

        print('MODERATOR: WELCOME TO ROCK, PAPER, SCISSOR 2023!')
        self.selection = selections
        self.user_score = user_score
        self.ai_score = ai_score

    def play_game(self):
        """PLay the Game of Rock, Paper, and Scissor"""

        # Walrus operator to continually get an input from the user until no input from the system exit
        while (user_input := input('Rock, Paper, or Scissor? >> ').strip().title()) not in system_exit:
            # Get an automatic AI input from the choices
            ai_input: str = choice(choices_selection)

            # Condition if the user enters an invalid selection
            if user_input not in choices_selection:
                print('MODERATOR: PLease Input a Valid Choice!\n')

            # another walrus operator to check if the game ends or not with game_result as its argument for the
            # result parameter
            if game_set := self.end_game(self.game_result(user_input, ai_input)):
                print(game_set)
                return  # exit the game

        else:
            print('MODERATOR: Quitting the System Please Wait....')
            time.sleep(3)

    def game_result(self, user_input: str, ai_input: str) -> str:
        """
        Get the USER and AI input and covert it to emoji and set the game result
        :param user_input: The user input (R, P, S)
        :param ai_input: The choice of the AI from the given choices
        :return str: The string result message either Win, Lose, or Tie
        """

        inputs = {'user': self.selection.get(user_input), 'computer': self.selection.get(ai_input)}

        # add the both string inputs and insert to tuple
        result: tuple = (user_input, ai_input)
        print(game_template.format(**inputs))

        # ternary operator
        return 'You Win' if result in win else 'AI Win' if result in lose else 'Its a Tie'

    def end_game(self, result: str) -> str:
        """
        Add a score from both AI and User based on the given result and decide the game if user or AI wins
        :param result: The result message return from game_result function
        :return str: The string end message of the game
        """

        # print the message result
        print(result, '\n')

        # condition to add score on both the user and ai score
        if result == 'You Win':
            self.user_score += 1
        elif result == 'AI Win':
            self.ai_score += 1

        # return the end game message if the user or AI wins
        return \
            f"You have Defeated the AI congratulations! with a score of ({self.user_score} vs. {self.ai_score})" \
            if self.user_score == 3 and self.ai_score < 3 \
            else f"You lose to AI...Better luck next time! with a score of ({self.user_score} vs. {self.ai_score})" \
            if self.ai_score == 3 and self.user_score < 3 \
            else ''


def main():
    """Main Function"""

    # converter >> str to emoji
    selection: dict = {
        "Rock": "🧱",
        "Paper": "📃",
        "Scissor": "✂"
    }

    # Create the object of the RSM class
    RSM_2023 = RSM(selection)
    RSM_2023.play_game()


if __name__ == '__main__':
    main()