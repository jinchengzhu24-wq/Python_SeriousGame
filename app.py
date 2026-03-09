from flask import Flask, render_template, request
from flask import redirect, url_for
from markupsafe import Markup, escape
import re

try:
    import markdown as markdown_lib
except ImportError:
    markdown_lib = None
from game.logic import GameLogic

app = Flask(__name__)

game = GameLogic()


def _render_basic_markdown(text):
    escaped = str(escape(text)).replace("\r\n", "\n")
    blocks = re.split(r"\n\s*\n", escaped.strip())
    rendered_blocks = []

    for block in blocks:
        lines = [line.strip() for line in block.split("\n") if line.strip()]
        if not lines:
            continue

        if all(line.startswith(("- ", "* ")) for line in lines):
            items = []
            for line in lines:
                content = re.sub(r"^[-*]\s+", "", line)
                items.append(f"<li>{content}</li>")
            rendered_blocks.append(f"<ul>{''.join(items)}</ul>")
            continue

        block_html = "<br>".join(lines)
        rendered_blocks.append(f"<p>{block_html}</p>")

    html = "".join(rendered_blocks)
    html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", html)
    html = re.sub(r"`([^`]+?)`", r"<code>\1</code>", html)
    return html


@app.template_filter("markdown")
def render_markdown(text):
    if not text:
        return ""

    if markdown_lib is None:
        return Markup(_render_basic_markdown(text))

    html = markdown_lib.markdown(
        text,
        extensions=["extra", "nl2br", "sane_lists"]
    )
    return Markup(html)


@app.route("/")
def index():
    game.reset()
    scenario = game.get_current_scenario()

    return render_template(
        "index.html",
        question=scenario["question"],
        options=scenario["options"],
        feedback=None,
        finished=False
    )


@app.route("/choose", methods=["POST"])
def choose():
    choice = request.form.get("choice")
    if not choice:
        return redirect(url_for("index"))

    feedback = game.process_choice(choice)

    if feedback is None:
        game.reset()
        scenario = game.get_current_scenario()
        return render_template(
            "index.html",
            question=scenario["question"],
            options=scenario["options"],
            feedback=None,
            finished=False
        )

    if game.is_game_finished():

        summary = game.get_summary()

        return render_template(
            "index.html",
            question=None,
            options=None,
            feedback=feedback,
            summary=summary,
            finished=True
        )

    else:

        scenario = game.get_current_scenario()

        return render_template(
            "index.html",
            question=scenario["question"],
            options=scenario["options"],
            feedback=feedback,
            finished=False
        )


if __name__ == "__main__":
    app.run(debug=True)
