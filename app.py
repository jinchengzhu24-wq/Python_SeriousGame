from flask import Flask, render_template, request
from game.logic import process_choice
from game.scenario import scenarios

app = Flask(__name__)

current_scenario = 0
choices_made = []


@app.route("/")
def index():

    global current_scenario, choices_made

    current_scenario = 0
    choices_made = []

    scenario = scenarios[current_scenario]

    return render_template("index.html", scenario=scenario)


@app.route("/result", methods=["POST"])
def result():

    global current_scenario, choices_made

    choice = request.form["choice"]

    choices_made.append(choice)

    current_scenario += 1

    if current_scenario < len(scenarios):

        scenario = scenarios[current_scenario]

        return render_template(
            "index.html",
            scenario=scenario
        )

    else:

        feedback = process_choice(choices_made)

        return render_template(
            "result.html",
            feedback=feedback
        )


if __name__ == "__main__":
    app.run(debug=True)