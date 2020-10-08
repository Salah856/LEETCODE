class Solution {
    static List<String> allPaths = new ArrayList<>();
     public static  void getPaths(TreeNode root, StringBuilder currentPath) {
        if (root != null) {
            currentPath.append(Integer.toString(root.val));
            if (root.left == null && root.right == null) {
                allPaths.add(currentPath.toString());
            }
            else {
                if (root.left != null)
                    getPaths(root.left, new StringBuilder(currentPath));
                if (root.right != null)
                    getPaths(root.right, new StringBuilder(currentPath));
            }
        }
    }
    public static int sumRootToLeaf(TreeNode root) {
        allPaths.clear();
        int num=0;
        getPaths(root, new StringBuilder());

        for(int i=0;i<allPaths.size();i++){
            String str = allPaths.get(i);
            int index =str.length()-1;
            int counter= 0;
            while (index>=0){
                num+=Character.getNumericValue(str.charAt(index))*Math.pow(2,counter);
                counter++;
                index--;
            }
        }
        return num;
    }
}
