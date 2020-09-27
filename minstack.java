class MinStack {


    Stack <Integer> stack = new Stack();
    Stack <Integer> minVals = new Stack();
    
    
    public void push(int x) {
        
        if(minVals.isEmpty() || x <= minVals.peek()){
            
            minVals.push(x);
        }

            
            stack.push(x);
        
    }
    
    public void pop() {
        
        if(stack.peek().equals( minVals.peek())){
            minVals.pop();
        }
        
        stack.pop();
        
        
    }
    
    public int top() {
        
        return stack.peek();
        
    }
    
    public int getMin() {
        
        return minVals.peek();
        
    }
}

