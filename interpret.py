class Solution(object):
    def interpret(self, command):
        
        o_c = command.count('()')
        al_c = command.count('(al)')
        
        for i in range(o_c):
            command = command.replace('()', 'o')
        
        for i in range(al_c):
            command = command.replace('(al)', 'al')
        
        return command
       
