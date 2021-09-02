func generateTrees(n int) []*TreeNode {
    return generateTreesInRange(1, n)
}

func generateTreesInRange(l, h int) []*TreeNode {
    if l > h { return []*TreeNode{nil} }
    if l == h { return []*TreeNode{{Val: l}} }
    res := make([]*TreeNode, 0)
    for i := l; i <= h; i++ {
        leftNodes := generateTreesInRange(l, i - 1)
        rightNodes := generateTreesInRange(i + 1, h)
        for _, leftNode := range leftNodes {
            for _, rightNode := range rightNodes {
                node := &TreeNode{i, leftNode, rightNode}
                res = append(res, node)
            }
        }
    }
    return res
}
