function [a, b] = regression(m, n)
    temp = m+n
    a = max(max(temp))
    b = min(min(temp))