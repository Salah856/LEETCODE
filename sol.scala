object Solution {
  import scala.collection.mutable
  
  /** 2D point and the collected keys bitset */
  type PointKeys = Int

  case class Point(r: Int, c: Int) {
    def up    = Point(r-1, c)
    def down  = Point(r+1, c)
    def left  = Point(r, c-1)
    def right = Point(r, c+1)
  }
  
  /** Current BFS state: current 2d point, bit set of collected keys, total number of moves */
  case class State(p: Point, bs: Int = 0, moves: Int = 0)
  
  /** @return compact encoded representation of PointKeys */
  def enc(point: Point, keysBs: Int): PointKeys = {
    // m = 30 -> 5 bits
    // n = 30 -> 5 bits
    // k      -> 5 bits
    import point.{r, c}
    
    r << 16 | c << 8 | keysBs
  }
  
  def isStart(c: Char)  = c == '@'
  def isWall(c: Char)   = c == '#'
  def isKey(c: Char)    = c.isLower
  def isLock(c: Char)   = c.isUpper
  def toKeyNum(c: Char) = c - 'a'
  def toKeyChar(n: Int) = (n + 'a').toChar
  
  def setHaveKey(bs: Int, c: Char): Int = {
    if (!isKey(c)) bs else {
      bs | 1 << toKeyNum(c)
    }
  }
  
  def haveKey(bs: Int, c: Char): Boolean = {
    (bs >> toKeyNum(c) & 1) == 1
  }
  
  def getAllKeys(keyCount: Int): Int = {
    var bs = 0
    for (key <- 0 until keyCount) {
      bs = setHaveKey(bs, toKeyChar(key))
    }
    bs
  }
  
  def findStartPoint(grid: Array[String]): Point = {
    val startPoints = for {
      r <- 0 until grid.length
      c <- 0 until grid(r).length
      if isStart(grid(r)(c))
    } yield {
      Point(r, c)
    }
    
    // assumes only one start point exists
    startPoints.head 
  }
  
  def findKeyCount(grid: Array[String]): Int = {
    val keys = for {
      row <- grid
      char <- row
      if isKey(char)
    } yield {
      ()
    }
    
    keys.length
  }
  
  def shortestPathAllKeys(g: Array[String]): Int = {
    val (m, n) = (g.length, g.head.length)

    val keyCount = findKeyCount(g)
    val allKeysBs = getAllKeys(keyCount)

    // BFS queue
    val q = mutable.Queue.empty[State]
    q += State(findStartPoint(g))
    
    // all previous explored BFS states: (row, col, collected keys bitset)
    val seen = mutable.Set.empty[PointKeys]
    
    def exploreIfPossible(p: Point, bs: Int, moves: Int): Unit = {
      val c = g(p.r)(p.c)
      if (!isWall(c) && (!isLock(c) || haveKey(bs, c))) {
        q += State(p, setHaveKey(bs, c), moves + 1)
      }
    }
	
    while (!q.isEmpty) {
      val State(p, bs, moves) = q.dequeue()
      
      if (bs == allKeysBs) {
        // all keys have been found
        return moves 
      }
      
      val encKey = enc(p, bs)
      
      if (!seen(encKey)) {
        seen += encKey
        
        if (p.r > 0)   exploreIfPossible(p.up,    bs, moves)
        if (p.r < m-1) exploreIfPossible(p.down,  bs, moves)
        if (p.c > 0)   exploreIfPossible(p.left,  bs, moves)
        if (p.c < n-1) exploreIfPossible(p.right, bs, moves)
      }
    }
    
    // no solution found
    -1
  }
}
