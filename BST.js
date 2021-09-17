var binaryTreePaths = function(node) {
    const paths = [];
    const dfs = (root, path) => {
        if (!root) return;
        
        const leaf = !root.left && !root.right;
        path = path.length ? path+'->' + root.val : String(root.val);
        if (leaf) {
            paths.push(path);
            return;
        }

        dfs(root.left, path);
        dfs(root.right, path);
    }
    
    dfs(node, '');
    
    return paths;
};
