def heuristic(a, b):
	return abs(a.i - b.i) + abs(a.j - b.j)


def get_sign(num):
    return 1 if num >= 0 else -1
