class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda p: p[1])
        arrows = 1
        arrow_x = points[0][1]
        for start, end in points[1:]:
            if start > arrow_x:   
                arrows += 1
                arrow_x = end
        return arrows
        
