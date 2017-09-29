# -*- encoding: utf-8 -*-

#
# [graph.py]
#
# A clone of @holman's Spark program to allow graphing of simple data in the terminal.
#
# Copyright (C) 2017, Liam Schumm. Licensed under the MIT License, included in LICENSE.rst.
#

ticks = ["▁", "▂", "▃", "▄", "▅", "▆ ", "▇ ", "█"]

def graph(*numbers_s):
    """graph: Graph numbers in your terminal.
    
    Usage:
        graph NUMBERS...
    """
    
    out = []
    
    for numbers in numbers_s:
        args = [int(x) for x in numbers]
    
        low = min(args)
        high = max(args)
        step = (high - low) / 8.0

        # if graph is constant, use highest character
        if low == high:
            return ticks[-1] * len(args)
    
        else:
            # string where completed graph goes
            s = ""
            for arg in args:
                for i in range(8):
                    if low + i * step <= arg <= low + (i+1) * step:
                        s += ticks[i]
            out.append(s)
    
    return out

exports = {'graph': graph}