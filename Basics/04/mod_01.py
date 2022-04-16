"""Scope Demo

Usage:
    python mod_01.py
"""

g = 420


def print_g():
    """Print G"""
    print(g)


def set_lg(inp):
    """Set local G"""
    g = inp


def set_gg(inp):
    """Set global G"""
    global g
    g = inp
