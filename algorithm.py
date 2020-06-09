from math import log
from utils import *
from functools import wraps

def memoize(function):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            val = function(*args)
            cache[args] = val
            return val
    return decorated_function


def sc(A, S):

    @memoize
    def ch(i, w):
        if w =='':
            return log(t[i], 2) if i in A.Final else float('inf')
        else:
            if i in A.delta and w[0] in A.delta[i]:
                return log(t[i],2) + min(ch(j, w[1:]) for j in A.delta[i][w[0]])
            else:
                return float('inf')

    s = list(A.Initial)[0]
    t = dict()

    for i in range(len(A.States)):
        t[i] = 1 if i in A.Final else 0
        if i in A.delta:
            t[i] += sum(map(len, A.delta[i].values())) #########
    return len(A.States) + sum(ch(s, w) for w in S) + A.countTransitions()*(2*log(len(A.States),2) \
        + log(len(A.Sigma),2))


def synthesize(S):
    A = buildPTA(S).toNFA()
    Red = {''}
    Blue = set(A.States)
    Blue.remove('')
    current_score = sc(A, S)
    while Blue:
        b = ql(Blue)[0]
        Blue.remove(b)
        for r in ql(Red):
            M = A.dup()
            merge(M.States.index(r), M.States.index(b), M)
            new_score = sc(M, S)
            if new_score < current_score:
                A = M
                current_score = new_score
                break
        if b in A.States:
            Red.add(b)
    return A


