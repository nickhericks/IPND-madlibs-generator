levels = ["easy", "medium", "hard"]

paragraphs = ['''A common first thing to do in a language is display 'Hello __1__!' In __2__ this is particularly
easy; all you have to do is type in: __3__ "Hello __1__!" Of course, that isn't a very useful thing to do.
However, it is an example of how to output to the user using the __3__ command, and produces a program which
does something, so it is useful in that capacity. It may seem a bit odd to do something in a Turing complete
language that can be done even more easily with an __4__ file in a browser, but it's a step in
learning __2__ syntax, and that's really its purpose.''',

'''A __1__ is created with the def keyword. You specify the inputs a __1__ takes by
adding __2__ separated by commas between the parentheses. __1__s by default return __3__ if you
don't specify the value to return. __2__ can be standard data types such as string, number, dictionary,
tuple, and __4__ or can be more complicated such as objects and lambda functions.''',

'''When you create a __1__, certain __2__s are automatically generated for you if you don't make
them manually. These contain multiple underscores before and after the word defining them.
When you write a __1__, you almost always include at least the __3__ __2__, defining
variables for when __4__s of the __1__ get made.''']

answers = [["world", "python", "print", "html"],
           ["function", "arguments", "none", "list"],
           ["class", "method", "__init__", "instance"]]

blanks = [["__1__", "__2__", "__3__", "__4__"],
          ["__1__", "__2__", "__3__", "__4__"],
          ["__1__", "__2__", "__3__", "__4__"]]


def level_select():
    '''
        Behavior:   Requests user input and loops until user input is in levels list.
        Inputs:     user input, levels list
        Outputs:    index of level selected in levels list
    '''
    user_input = ""
    while user_input not in levels:
        user_input = raw_input("\n\nPlease select a game difficulty by typing it in!\nPossible choices include easy, medium, and hard. ")
        if user_input not in levels:
            print "That's not an option!"
    index = levels.index(user_input)
    print "\n\nYou've chosen: " + levels[index] + "\nYou will get 5 guesses per problem."
    return index


def ask_question(index, counter, blank):
    '''
        Behavior:   Requests user_input, checks for correctness, and keeps track of wrong guesses.
        Inputs:     index, counter, blank, user_input
        Outputs:    user_input if correct, otherwise None
    '''
    user_input = ""
    guesses = 0
    max_guesses = 5
    while user_input != answers[index][counter]:
        user_input = raw_input("\nWhat should be substituted in for " + blank + "? ")
        if user_input != answers[index][counter]:
            guesses += 1
            if guesses == max_guesses:
                return None
            elif guesses == max_guesses - 1:
                print "That isn't the correct answer! You only have 1 try left! Make it count!"
            else:
                print "That isn't the correct answer! Let's try again; you have " + str(max_guesses - guesses) + " tries left!"
    return user_input


def fill_blank(index):
    '''
        Behavior:   Takes in index and uses it to find correct index for paragraph, answer and the blank list,
                    passes those to ask_question function and then updates paragraph.
        Inputs:     index, paragraph
        Outputs:    if user_input correct returns paragraph updated with correct word
                    if user_input is incorrect returns None
    '''
    new_paragraph = paragraphs[index]
    for each in blanks[index]:
        counter = blanks[index].index(each)
        blank = blanks[index][counter]
        answer = answers[index][counter]
        print "\n\nThe current paragraph reads as such:\n\n" + new_paragraph
        user_input = ask_question(index, counter, blank)
        if user_input != answer:
            return None
        print "\nCorrect!\n"
        new_paragraph = new_paragraph.replace(blank, user_input)
    return new_paragraph


def play_game():
    '''
        Behavior:   This function starts when the program is run and it coordinates the structure of the game.
        Inputs:     Takes no inputs
        Outputs:    Returns no value
    '''
    index = level_select()
    completed = fill_blank(index)
    if completed == None:
        print "You've failed. Too many incorrect guesses. Game over!"
        return
    print completed
    print "\nYou won!\n\n"
    return

play_game()
