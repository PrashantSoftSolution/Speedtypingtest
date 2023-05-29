import time

def check_typing():
    text = "whatever data you want to enter: "
    print("Type the data whatever you've: ")
    print(text)

    input("Press Enter to the start your typing: ")
    start_time = time.time()

    user_input = input()

    end_time = time.time()
    elapsed_time = end_time - start_time

    user_input = user_input.strip().lower()
    text = text.lower()


    correct_chars = sum([1 for i in range(len(text)) if text[i] == user_input[i]])
    accuracy = (correct_chars / len(text)) * 100

    
    num_words = len(text.split())
    wpm = (num_words / elapsed_time) * 60

    print("\n---------RESULT---------")
    print("Time elapsed: {:.2f} sec".format(elapsed_time))
    print("Your Accuracy: {:.2f}%".format(accuracy))
    print("Words per minute: {:.2f} WPM".format(wpm))

check_typing()
