import sys
from common import parse_file, is_feasible


def matching_bs(a, B):
	matching_bs =  []
	for b in B:
		if a in b:
			matching_bs.append(b)

	return matching_bs	


def sort_most_matched_elements(A, B):
	a_with_matching_bs = []
	for a in A:
		mbs = matching_bs(a, B)
		a_with_matching_bs.append((a, mbs))

	return sorted(a_with_matching_bs, key=lambda a_s : len(a_s[1]), reverse=True)

def greedy_hitting_set(A, B):
	C = set()
	while not len(B) == 0: 
		sorted_as_with_matching_bs = sort_most_matched_elements(A, B)
		(most_matched_a, matching_bs) = sorted_as_with_matching_bs[0]
		print(most_matched_a, matching_bs)
		B = list(set(B) - set(matching_bs))
		C.add(most_matched_a)
		A.remove(most_matched_a)

	return C

 
def main():
    argv = sys.argv
    if len(argv) != 2:
        print('Usage: python3 greedy.py <filename>')
        return

    filename = argv[1]

    A, B = parse_file(filename)
    C = greedy_hitting_set(A, B)
    print(C)


if __name__ == '__main__':
    main()

    