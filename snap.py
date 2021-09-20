class SnapshotArray:
    
    def __init__(self, length: int):
        self.snaps = []
        self.current = {}

    def set(self, index: int, val: int) -> None:
        
        self.current[index] = val;

    def snap(self) -> int:
        
        self.snaps.append(dict(self.current))
        
        return len(self.snaps)-1
		
    def get(self, index: int, snap_id: int) -> int:
        
        snap = self.snaps[snap_id]
        
        if index in snap:
            return snap[index]
        
        return 0

