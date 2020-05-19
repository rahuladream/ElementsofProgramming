class StockSpanner:
    
    def __init__(self):
        self.monotone_stack = []
              
    def next(self, price: int) -> int:

        stack = self.monotone_stack
        
        cur_price_quote, cur_price_span = price, 1
        
        while stack and stack[-1][0] <= cur_price_quote:
            
            prev_price_quote, prev_price_span = stack.pop()
            
            cur_price_span += prev_price_span
        stack.append( (cur_price_quote, cur_price_span) )
        
        return cur_price_span

if __name__ == "__main__":
    S = StockSpanner()
    print( S.next(100) )    # returns 1
    print( S.next(80) )     # returns 1
    print( S.next(60) )     # returns 1
    print( S.next(70) )     # returns 2
    print( S.next(60) )     # returns 1
    print( S.next(75) )     # returns 4
    print( S.next(85) )     # returns 4