
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
                print(new)
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

    print(start, end)

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
        # top_frontier = expand_node_top(start, 0, (1, 1))
        # bot_frontier = expand_node_bot(end, 0, (-1, -1))

        # expand top
        while 0==0:
            # SEARCH DOWN
            for fnode in top_frontier:
                # expand by 1 in all directions
                for dirx in [(0, 1), (1, 0), (1, 1)]:
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
                for dirx in [(0, -1), (-1, 0), (-1, -1)]:
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

    cur = p

    return path


def mm_alg():
    """
    Initial call for linear space MM Algorithm
    """
    global u, v
    global ppoints

    # linked list
    start = (0 , 0)
    end = (len(u)+1, len(v)+1)

    ppoints = {}
    # to the point in front of it
    ppoints[start] = None
    ppoints[end] = None

    find_points(start, end)

    print(ppoints)

    path = create_path(ppoints)

    alignment, score = create_alignment(path)

    return alignment, score


if __name__ == "__main__":
    # strings
    global u, v

    u = "ABCAC"
    v = "ACBC"

    mm_alg()
