#! /usr/bin/env python3

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        hash_map = [[0 for _ in range(11)]for _ in range(n)]
        winners = 0
        for player in pick:
            plr,ball = player
            hash_map[plr][ball]+=1
        index = 0
        for player in hash_map:
            for ball in player:
                if ball > index:
                    winners +=1
                    break
            index +=1
        return winners
