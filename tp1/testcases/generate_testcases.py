import random


# Generate two random number between 1 and 10000
def random_number():
    return (random.randint(1, 10000), random.randint(1, 10000))


# Generate a list of random numbers
def random_list(n):
    return [random_number() for i in range(n)]


# Generate a list of random numbers and write it to a file
def random_list_to_file(n, filename):
    with open(filename, "w") as file:
        file.write("S_i,A_i" + "\n")
        for i in range(n):
            si, ai = random_number()
            file.write(str(si) + ", " + str(ai) + "\n")


if __name__ == "__main__":
    for i in range(1000):
        if i == 0:
            continue
        filename = "testcase_" + str(i * 100) + ".txt"
        random_list_to_file(i * 100, filename)
        print("Generated " + filename)
