"""
This contains validation for the AI quiz.
"""


def validate_name(name):
    """
    This function ensures the user has entered a name in the box.
    User enters name:
        name (str): User's name
    Returns:
        True if text is written, False if nothing is entered
    """

    if name.strip() == "":
        return False

    return True