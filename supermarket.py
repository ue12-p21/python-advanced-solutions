def queue_time(customers, n):
    """
    solution to
    https://www.codewars.com/kata/57b06f90e298a7b53d000a86
    """
    # model the queues
    queues = n *[0]
    while customers:
        next = customers.pop(0)
        # this could be optimized as we are exactly
        # one swap away from a sorted list at this point
        # so:
        # (*) a dichotomy would yield a log(n) complexity instead
        # (*) easier still, use a heapq to efficiently preserve
        #     the sortedness invariant - see below
        queues.sort()
        # put the biggest customer is the shallowest queue
        queues[0] += next
    # we're done
    return max(queues)

#
# using a heapq
#
# here is e.g. another implementation
# using a heapq
# https://docs.python.org/3/library/heapq.html
#
#
import heapq

def queue_time_bis(customers, n):
    queues = n *[0]
    # just transform the list into a heapq
    heapq.heapify(queues)
    while customers:
        next = customers.pop(0)
        # getting and removing the smallest
        free_counter = heapq.heappop(queues)
        # adding the sum
        heapq.heappush(queues, free_counter + next)
    # we're done
    return max(queues)
