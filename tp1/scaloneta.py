import sys


class MatchReview:
    def __init__(self, si, ai):
        self.si = si  # coach analysis duration
        self.ai = ai  # helper analysis duration

    def __str__(self):
        return "Si: " + str(self.si) + ", Ai: " + str(self.ai)

    def __lt__(self, otherReview):
        return self.ai > otherReview.ai or (
            self.ai == otherReview.ai and self.si < otherReview.si
        )

    def __eq__(self, otherReview):
        return self.ai == otherReview.ai and self.si == otherReview.si

def show_reviews(review_list):
    print("Matches will be reviewed in the following order:")
    i = 1
    for r in review_list:
        print("Match " + str(i) + ": " + str(r))
        i += 1

def read_reviews_file(filename):
    review_list = []
    with open(filename, "r") as file:
        for line in file:
            si, ai = line.split(",")

            if not si.strip().isdigit() or not ai.strip().isdigit():
                continue

            mr = MatchReview(int(si), int(ai))
            review_list.append(mr)

    return review_list


def sort_reviews(review_list):
    return sorted(review_list)


def full_review_time(review_list):
    curr_si = 0
    curr_ai = 0

    for review in review_list:
        curr_si += review.si
        curr_ai = max(curr_ai, curr_si + review.ai)

    return curr_ai


def main():
    if len(sys.argv) != 2:
        print(
            "Incorrect amount of arguments. " + "Usage: " + sys.argv[0] + " <filename>"
        )
        return

    try:
        review_list = read_reviews_file(sys.argv[1])
        sorted_review_list = sort_reviews(review_list)
        show_reviews(sorted_review_list)

        print("Full analysis duration is:")
        print(full_review_time(sorted_review_list))
    except:
        print("Error reading file " + sys.argv[1] + ". Check file format.")
        return

if __name__ == "__main__":
    main()
