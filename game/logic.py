from game.scenario import scenarios
from game.feedback import generate_feedback, generate_summary

class GameLogic:

    def __init__(self):
        self.reset()

    def reset(self):
        self.current_index = 0
        self.history = []

    def get_current_scenario(self):
        if self.current_index < len(scenarios):
            return scenarios[self.current_index]
        return None

    def process_choice(self, choice):
        if self.is_game_finished():
            return None

        scenario = scenarios[self.current_index]["question"]

        feedback = generate_feedback(scenario, choice)

        self.history.append({
            "scenario": scenario,
            "choice": choice
        })

        self.current_index += 1

        return feedback

    def is_game_finished(self):
        return self.current_index >= len(scenarios)

    def get_summary(self):
        return generate_summary(self.history)
