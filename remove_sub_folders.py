class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder_set = set(folder)
        
        def is_subfolder(f):
            folders = f.split("/")
            folders.pop(0) # remove empty string
            
            curr_dir = ""
            folder_set.remove(f)
            for fold in folders:
                curr_dir += "/" + fold
                if curr_dir in folder_set:
                    return True
            folder_set.add(f)
            return False
        
        ans = []
        for f in folder:
            if not is_subfolder(f):
                ans.append(f)
        return ans
