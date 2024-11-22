class Solution:
    def judgeCircle(self, moves: str) -> bool:
        RBx = 0
        RBy = 0
        move_list = {
            "L" : -1,
            "R" : 1,
            "U" : 1,
            "D" : -1
        }
        for move in moves:
            if move == "L" or move == "R":
                RBx += move_list[move]
            else:
                RBy += move_list[move]
        return True if RBx == 0 and RBy == 0 else False
