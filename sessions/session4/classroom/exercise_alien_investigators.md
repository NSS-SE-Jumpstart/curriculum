# Exercise - Alien Investigators

In this exercise you'll build a tool for choosing a team of brave souls to investigate a possibly alien-infested forest.

You'll start out with some existing code, but it isn't complete and has a few bugs in it. Your task is to fix the bugs and complete the code.

## Setup

1. Create a new Python file called `alien_investigators.py` and copy the following code into it.

    ```python
    team_options = [
        "Harvey (Physicist)",
        "Wendy (Has a really good flashlight)",
        "Andre (Owns the forest)",
        "Julie (Biologist)",
        "Cleetus (Self-proclaimed expert on things)",
        "Marlowe (Private Investigator)",
        "Brian (Talks to animals)",
        "Joan (Zealot)",
        "Winston (Agreed to be alien bait)",
        "Landrel (Anthropologist)",
        "Marvin (Photographer)",
        "Linda (Conspiracy Nut)"
    ]

    print("\033[H\033[J")
    print("There have reports of strange lights in the forest.")
    print("The locals believe aliens have landed and are trying to recruit woodland creatures for their dastardly schemes.")
    print("Your job is to assemble a team of investigators to check out the forest to find out what's really going on.")
    print("---")
    print()

    team = []

    for option in team_options:
        print("\033[H\033[J")

        print("Team so far:")
        for member in team:
            print("  " + member)

        print()
        choice = input("Include '" + option + "'? (y/n) ")
        if choice == "y":
            team.append(option)


    leader = team[0]
    team.remove(leader)
    print("Team Leader: " + leader)

    print("And the rest of the team:")
    for member in team:
        print("  " + member)
    ```

1. Examine the code to get a sense of what it does, then run it to see if you were right.

## Bug Fixes

1. When the program starts, the user should see a brief message that describes the program's purpose. Unfortunately, this message doesn't appear to be working. Fix it.

    > **NOTE:** The message should disappear after the user responds to the first `input()` prompt.

1. In the event that the user does not select any of the available options, they see a nasty error message.

    ```text
    Traceback (most recent call last):
      File "alien_investigators.py", line 38, in <module>
        leader = team[0]
    IndexError: list index out of range
    ```

    Prevent this error message from being displayed.

## New Features

1. If the user does not select anyone to be on the team, display a message indicating they should re-run the program to create a team.
1. Update the code to prevent the display of the `Team so far:` message if the `team` list is empty.
1. Right now the code assumes the first person who is chosen is the team leader, but this isn't very flexible.

    Update the code so that if, _and only if,_ a person is chosen to be on the team, the user is asked if that person should be the leader. If the user enters a `y`, insert the person into the first element of the list, otherwise append them to the end of the list.
