from FAdo.fa import *

def alphabet(S):
    result = set()
    for s in S:
        for a in s:
            result.add(a)
    return result


def prefixes(S):
    result = set()
    for s in S:
        for i in range(len(s) +1 ):
            result.add(s[:i])
    return result


def suffixes(S):
    result = set()
    for s in S:
        for i in range(len(s)+1):
            result.add(s[i:1])
    return result


def catenate(A, B):
    return set(a+b for a in A for b in B)


def ql(S):
    return sorted(S, key= lambda x: (len(x), x))


def buildPTA(S):
    A = DFA()
    q = dict()

    for u in prefixes(S):
        q[u] = A.addState(u)

    for w in iter(q):
        u, a = w[:-1], w[-1:]
        if a !='':
            A.addTransition(q[u], a, q[w])
        if w in S:
            A.addFinal(q[w])
    A.setInitial(q[''])
    return A


def merge(q1, q2, A):
    n = len(A.States)
    for q in range(n):
        if q in A.delta:
            for a in A.delta[q]:
                if q2 in A.delta[q][a]:
                    A.addTransition(q, a, q1)
        if q2 in A.delta:
            for a in A.delta[q2]:
                if q in A.delta[q2][a]:
                    A.addTransition(q1, a, q)
    if q2 in A.Initial:
        A.addInitial(q1)
    if q2 in A.Final:
        A.addFinal(q1)
    A.deleteStates([q2])
    return A


def accepts(w, q, A):
    ilist = A.epsilonClosure(q)
    for c in w:
        ilist = A.evalSymbol(ilist, c)
        if not ilist:
            return False
    return not A.Final.isdisjoint(ilist)


