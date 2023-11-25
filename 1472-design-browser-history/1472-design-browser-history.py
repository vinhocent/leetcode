class BrowserHistory:

    def __init__(self, homepage: str):
        self.array = []
        self.array.append(homepage)
        self.totalPages = 0
        self.currPage = 0
        

    def visit(self, url: str) -> None:
        
        if len(self.array) - 1 > self.currPage:
            self.array[self.currPage + 1] = url
        else:
            self.array.append(url)
            
        self.currPage += 1
        self.totalPages = self.currPage
        

    def back(self, steps: int) -> str:
        
        self.currPage = max(0, self.currPage - steps)
        
        return self.array[self.currPage]

    def forward(self, steps: int) -> str:
        
        self.currPage = min(self.totalPages, self.currPage + steps)
        
        return self.array[self.currPage]
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)