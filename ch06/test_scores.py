#!/usr/bin/env python3

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = []
    while True:
        score = int(input("Enter test score: "))
        if score >= 0 and score <= 100:
            scores.append(score)
        else:
            print("Test score must be from 0 through 100. Score discarded. Try again.")
        continue_entry = input("Enter another score (y/n)? ")
        if continue_entry.lower() != "y":
            break
    return scores

def process_scores(scores):
    total = sum(scores)
    average = total / len(scores)
    scores.sort()
    if len(scores) % 2 == 0:
        median = (scores[len(scores) // 2 - 1] + scores[len(scores) // 2]) / 2
    else:
        median = scores[len(scores) // 2]
    print(f"Score count:       {len(scores)}")
    print(f"Score total:       {total}")
    print(f"Average score:     {average}")
    print(f"Low score:         {min(scores)}")
    print(f"High score:        {max(scores)}")
    print(f"Median score:      {median}")

def main():
    scores = get_scores()
    process_scores(scores)

if __name__ == "__main__":
    main()


