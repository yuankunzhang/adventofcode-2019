#!/usr/bin/env python
# -*- coding: utf-8 -*-


def calc_indegree(graph, vertex):
    for edge in graph[vertex]['edges']:
        graph[edge]['indegree'] += 1
        graph[edge]['orbits'] += graph[vertex]['orbits'] + 1
        calc_indegree(graph, edge)


def build_graph(orbits):
    graph = {}

    for orbit in orbits:
        a, b = orbit.split(')')
        if a not in graph:
            graph[a] = {
                'indegree': 0,
                'orbits': 0,
                'edges': [],
                'reverse-edges': [],
            }
        if b not in graph:
            graph[b] = {
                'indegree': 0,
                'orbits': 0,
                'edges': [],
                'reverse-edges': [],
            }
        graph[a]['edges'].append(b)
        graph[b]['reverse-edges'].append(a)

    calc_indegree(graph, 'COM')
    return graph


def count_orbits(graph, vertex):
    count = graph[vertex]['orbits']
    for edge in graph[vertex]['edges']:
        count += count_orbits(graph, edge)
    return count


def shortest_path(graph, v0, v1, visited):
    if v0 == v1:
        return 0

    visited.append(v0)
    edges = [v for v in graph[v0]['edges'] if v not in visited]
    edges += [v for v in graph[v0]['reverse-edges'] if v not in visited]
    if not edges:
        return float('inf')
    return min([shortest_path(graph, v, v1, visited) for v in edges]) + 1


def part1():
    data = [x.strip() for x in open('input').readlines()]
    graph = build_graph(data)
    return count_orbits(graph, 'COM')


def part2():
    data = [x.strip() for x in open('input').readlines()]
    graph = build_graph(data)
    return shortest_path(graph, 'YOU', 'SAN', []) - 2


print('part1:', part1())
print('part2:', part2())
