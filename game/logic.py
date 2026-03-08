def process_choice(choices):

    score = 0

    negative = [
        "Reply angrily",
        "Respond with insults",
        "Respond sarcastically"
    ]

    neutral = [
        "Ignore the comment",
        "Ignore and move on",
        "Stop responding"
    ]

    positive = [
        "Explain calmly",
        "Ask what they mean",
        "Explain your idea politely"
    ]


    for choice in choices:

        if choice in negative:
            score -= 1

        elif choice in positive:
            score += 1


    if score <= -2:
        return "Your responses may escalate online conflict."

    elif score == 0:
        return "Your responses are neutral."

    else:
        return "Your responses show constructive communication."