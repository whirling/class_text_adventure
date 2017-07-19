start = '''
You are sitting in your Macroeconomics class. Your teacher's name is Mr. Davenport, and he doesn't like you.
There are 5 minutes left in the period. Your goal is to make it to your next class, Birdhouse Woodcrafting Class, on time and without disappointing your Birdhouse Woodcrafting instructor.
'''
print(start)

pack_time_dialogue = '''
Do you
1. Pack up your things now
2. Wait until the bell rings?
Type 'now' or 'later'
'''
print(pack_time_dialogue)
pack_time = input()
if pack_time == "now":
    print("Mr. Davenport is not impressed with your childish shenanigans. He holds the class two minutes after the bell to satisfy his superiority complex. You are late to Birdhouse Woodcrafting Class and your Birdhouse Woodcrafting instructor is deeply disappointed in you.")
elif pack_time == "later":
    later_choice_dialogue = '''
    You won't be able to pack up quickly enough! Will you
    1. Leave your belongings behind;
        if you love something set it free /
        if it comes back it's yours /
        if not, it was never meant to be
    2. Pack them away lovingly. You could never be so coldhearted!
    3. Just grab all of your things in your arms and carry them to your next class.
    Type 'leave' to respect the autonomy of your school supplies
         'pack' to protect them from the harsh realities of life
         'carry' to haphazardly trundle them into your favorite class: Birdhouse Woodcrafting, with your favorite teacher, your Birdhouse Woodcrafting instructor.
    '''
    print(later_choice_dialogue)
    later_choice = input()
    if later_choice == "leave":
        print("You arrive to Birdhouse Woodcrafting class on time, but have none of your chisels. You are marked unprepared and your Birdhouse Woodcrafting instructor is deeply disappointed in you.")
    elif later_choice == "pack":
        print("You are late to Birdhouse Woodcrafting Class and your Birdhouse Woodcrafting instructor is deeply disappointed in you.")
    elif later_choice == "carry":
        carry_choice_dialogue = '''
        You are in a scrambling blitz of a dash, so you don't realize that your supplies are a little heavier than usual until you are in the hallway. Do you
        1. Check through your things to make sure they are all your own
        2. Ignore this epiphany and canter to class. You don't want to be late to Birdhouse Woodcrafting!
        Type 'check' to rummage through the pile in your arms
             'scram' to skedaddle with nary a thought
        '''
        print(carry_choice_dialogue)
        carry_choice = input()
        if carry_choice == "scram":
            print("You are arrested for Grand Theft Toaster. Your Birdhouse Woodcrafting instructor is deeply disappointed in you.")
        elif carry_choice == "check":
            check_choice_dialogue = '''
            You see that you have accidentally acquired Mr. Davenport's Toastmaster BTW09 Pop-Up 4 Slice Bun & Bagel Toaster 120V! Do you
            1. Apologize profusely and return the Toastmaster immediately
            2. Set it down on the ground and inch away casually, whistling 'Tiptoe Through the Tulips'
            3. Take it with you. Score!
            Type 'grovel' to return the appliance in question
                 'depart' to pretend you'd never swiped the unsuspecting 4 Slice
                 'keep' to enjoy your new Toastmaster
            '''
            print(check_choice_dialogue)
            check_choice = input()
            if check_choice == "grovel":
                print("Mr. Davenport enjoys your pain, and keeps you there for twenty minutes. You are late to Birdhouse Woodcrafting Class and your Birdhouse Woodcrafting instructor is deeply disappointed in you.")
            elif check_choice == "keep":
                print("You are arrested for Grand Theft Toaster. Your Birdhouse Woodcrafting instructor is deeply disappointed in you.")
            elif check_choice == "depart":
                print("You make it to Birdhouse Woodcrafting class on time, and you have all of your chisels. Your Birdhouse Woodcrafting instructor is proud of you. You are happy.")
