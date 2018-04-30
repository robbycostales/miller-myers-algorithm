

def expand_node(node, by, dirx):
    '''
    Expands the path of a node by a score of one in all directions. Is called recursively. If score is 0, the path can be expanded by 1, if the score is 1, look for all free paths (along the diagonal)

    Args:
        node (tuple) - position
        by (int)- value to expand node by
        dirx (tuple) - 2-tuple with 1s, -1s, and 0s

    Returns the new set of "frontier" nodes that are discovered from that expansion by 1 or 0 (as a list)
    '''

    




def find_points(start, end):
    """
    Finds path for mm_alg
    """
    global u, v
    global ppoints

    if end == start:
        # deal with connections if start and end are near
        # NOTE may need to fix condition above
    else:
        # first expand start and end by length 0 if possible
        top_frontier = expand_node(start, 0, (1, 1))
        bot_frontier = expand_node(end, 0, (-1, -1))

        # expand top
        while 0==0:
            new_top_frontier = []
            for fnode in top_frontier:
                # expand by 1 in all directions
                for dirx in [(0, 1), (1, 0), (1, 1)]:
                    temp = expand_node(fnode, 1, dirx)
                    # check to see if any of the new frontier nodes are in
                    for i in temp:
                        if i in bot_frontier:
                            upper = fnode
                            lower = i
                            # save connection in path
                            ppoints[upper] = lower
                            # recursive call
                            find_points(start, upper)
                            find_points(lower, end)
                            return
                    # add found nodes to new frontier
                    new_top_frontier += temp
            # take all unique values of new_top_frontier
            top_frontier = list(set(new_top_frontier))






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

    path = create_path(ppoints)

    alignment, score = create_alignment(path)

    return alignment, score


if __name__ == "__main__":
    # strings
    global u, v

    u = "AAAGAATTCA "
    v = "AAATCA"
