
def expand_node_bot(node, by, dirx):
    '''
    '''
    global u, v
    global ppoints
    global top_frontier, bot_frontier
    global new_top_frontier, new_bot_frontier

    new = (node[0] + dirx[0], node[1] + dirx[1])

    if new[0] > len(u) or new[0] < 0 or new[1] > len(v) or new[1] < 0:
        return False, (None, None)

    if new in top_frontier:
        # since bottom frontier, node points to new
        ppoints[new] = node
        up = new
        down = node
        return True, (up, down)
    elif new in bot_frontier:
        # we don't want to store a node already in our frontier
        # we would do more computation than needed
        return False, (None, None)
    else:
        if by == 1:
            new_bot_frontier.append(new)
            # if moving diagonal
            if dirx == (-1, -1):
                # if the characters are equal
                if u[new[0]-1] == v[new[1]-1]:
                    # can still spare one more move
                    for x in [(0, -1), (-1, 0), (-1, -1)]:
                        found, (up, down) = expand_node_bot(new, 1, x)
                        if found:
                            return found, (up, down)
                # if the characters are not equal
                else:
                    found, (up, down) = expand_node_bot(new, 0, (-1, -1))
                    if found:
                        return found, (up, down)
            # if moving horizontal or vertical
            else:
                return False, (None, None)

        elif by == 0:
            # only move is diagonal
            if dirx == (-1, -1):
                # if the characters are equal
                if u[new[0]-1] == v[new[1]-1]:
                    new_bot_frontier.append(new)
                    found, (up, down) = expand_node_bot(new, 0, (-1, -1))
                # if characters are not equal
                else:
                    # if by is 0, characters are not equal, we cannot expand more
                    return False, (None, None)
            else:
                raise

        else:
            raise

        return False, (None, None)


def expand_node_top(node, by, dirx):
    '''
    '''
    global u, v
    global ppoints
    global top_frontier, bot_frontier
    global new_top_frontier, new_bot_frontier

    new = (node[0] + dirx[0], node[1] + dirx[1])

    if new[0] > len(u) or new[0] < 0 or new[1] > len(v) or new[1] < 0:
        return False, (None, None)

    if new in bot_frontier:
        # since top frontier, node points to new
        ppoints[node] = new
        up = node
        down = new
        return True, (up, down)
    elif new in top_frontier:
        # we don't want to store a node already in our frontier
        # we would do more computation than needed
        return False, (None, None)
    else:
        if by == 1:
            new_top_frontier.append(new)
            # if moving diagonal
            if dirx == (1, 1):
                # if the characters are equal
                if u[new[0]-1] == v[new[1]-1]:
                    # can still spare one more move
                    for x in [(0, 1), (1, 0), (1, 1)]:
                        found, (up, down) = expand_node_top(new, 1, x)
                        if found:
                            return found, (up, down)
                # if the characters are not equal
                else:
                    found, (up, down) = expand_node_top(new, 0, (1, 1))
                    if found:
                        return found, (up, down)
            # if moving horizontal or vertical
            else:
                return False, (None, None)

        elif by == 0:
            # only move is diagonal
            if dirx == (1, 1):
                # if the characters are equal
                if u[new[0]-2] == v[new[1]-2]:
                    new_top_frontier.append(new)
                    found, (up, down) = expand_node_top(new, 0, (1, 1))
                # if characters are not equal
                else:
                    # if by is 0, characters are not equal, we cannot expand more
                    return False, (None, None)
            else:
                raise

        else:
            raise

        return False, (None, None)


def find_points(start, end):
    """
    Finds path for mm_alg
    """
    global u, v
    global ppoints
    global top_frontier, bot_frontier
    global new_top_frontier, new_bot_frontier

    new_top_frontier = []
    new_bot_frontier = []
    top_frontier = [start]
    bot_frontier = [end]

    if start == end:
        # deal with connections if start and end are near
        # NOTE may need to fix condition above
        return
    else:
        # first expand start and end by length 0 if possible

        # NOTE: START OF F'D UP STUFF

        found, (up, down) = expand_node_top(start, 0, (1, 1))
        if found:
            find_points(start, up)
            find_points(down, end)
            return
        if new_top_frontier != []:
            top_frontier = list(set(new_top_frontier))
            new_top_frontier = []

        found, (up, down) = expand_node_bot(end, 0, (-1, -1))
        if found:
            find_points(start, up)
            find_points(down, end)
            return
        if new_bot_frontier != []:
            bot_frontier = list(set(new_bot_frontier))
            new_bot_frontier = []

        # NOTE: END OF F'D UP STUFF

        # expand top
        while 0==0:
            # SEARCH DOWN
            for fnode in top_frontier:
                # expand by 1 in all directions
                for dirx in [(1, 1), (0, 1), (1, 0)]:
                    found, (up, down) = expand_node_top(fnode, 1, dirx)
                    if found:
                        find_points(start, up)
                        find_points(down, end)
                        return
            # take all unique values of new_top_frontier
            top_frontier = list(set(new_top_frontier))

            # SEARCH UP
            for fnode in bot_frontier:
                # expand by 1 in all directions
                for dirx in [(-1, -1), (0, -1), (-1, 0)]:
                    found, (up, down) = expand_node_bot(fnode, 1, dirx)
                    if found:
                        find_points(start, up)
                        find_points(down, end)
                        return
            # take all unique values of new_top_frontier
            bot_frontier = list(set(new_bot_frontier))


def create_path():
    global ppoints

    path = []

    cur = (0, 0)
    while cur != None:
        cur = ppoints[cur]
        path.append(cur)

    # remove last two
    path = path[:-1]

    # subtract 1 from each index (to get indices of string, not matrix)
    for i in range(len(path)):
        path[i] = (path[i][0]-1, path[i][1]-1)

    return path


def create_alignment():
    global path
    # alignment
    alignment = []
    # the first value is always (0,0)
    prev = (0, 0)
    # we skip the first value
    distance = 0
    for val in path[1:]:
        if tm(val, prev) == (1, 1):
            # if diagonal
            alignment.append((u[prev[0]], v[prev[1]]))
            if u[prev[0]] != v[prev[1]]:
                distance += 1
        elif tm(val, prev) == (1, 0):
            alignment.append((u[prev[0]], "-"))
            distance += 1
        elif tm(val, prev) == (0, 1):
            alignment.append(("-", v[prev[1]]))
            distance += 1

        prev = val



    return alignment, distance


def tm(t1, t2):
    # tup minus
    return (t1[0]-t2[0], t1[1]-t2[1])


def mm_alg():
    """
    Initial call for linear space MM Algorithm
    """
    global u, v
    global ppoints
    global path

    # linked list
    start = (0 , 0)
    end = (len(u)+1, len(v)+1)

    ppoints = {}
    # to the point in front of it
    ppoints[start] = None
    ppoints[end] = None

    find_points(start, end)

    path = create_path()

    alignment, distance = create_alignment()

    return alignment, distance


if __name__ == "__main__":
    # strings
    global u, v


    # SET STRINGS HERE
    u = "asdflkjdfj"
    v = "asdfjsdjkfj"

    a, d = mm_alg()

    print("Alignment:\n")
    for i in a:
        print(i)
    print("\n\nDistance:\n\n{}".format(d))
