class Solution:
    def dayOfYear(self, date: str) -> int:
        
        days_in_month = [31,28,31,30,31,30,31,31,30,31,30]
        year, month, day = list(map(int, date.split('-')))
        
        if month == 1:
            return day
        
        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            days_in_month[1] += 1
        
        
        return sum(days_in_month[:month-1]) + day
