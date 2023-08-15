import time

def typing_speed():
    # Prompt the user to start typing
    input("Press enter to start typing:")

    # Gets current time
    start_time = time.time()

    # The sentence the person has to write
    sentence = "The quick brown fox jumps over the lay dog"
    user_input = input(f'Type this sentence "{sentence}"\n')

    # Gets the current time again
    end_time = time.time()

    # Calculate the time taken to type
    time_taken = end_time - start_time

    # Calculate the typing speed
    word_per_minute = len(user_input.split()) / time_taken * 60

    # Display the typing speed
    print(f'Type speed: {word_per_minute:.2f} words per minute')

typing_speed()