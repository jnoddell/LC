using namespace std;

class BrowserHistory {
    
private:
    
    vector<string> stack;
    int pos;
    
public:
    
    BrowserHistory(string homepage) {
        
        stack.push_back(homepage);
        this->pos = 0;
    
    }
    
    void visit(string url) {
        
        int initSize = this->stack.size();
        for( int i = this->pos + 1; i < initSize; i++)
            this->stack.pop_back();
        
        this->stack.push_back( url );
        this->pos++;
        
    }
    
    string back(int steps) {
        
        int dx = steps;

        if (this->pos - steps < 0) dx = this->pos;
        
        this->pos -= dx;
        
        return this->stack[this->pos];
        
    }
    
    string forward(int steps) {
        
        int dx = steps;
        
        if (this->pos + steps > this->stack.size() - 1) dx = this->stack.size() - this->pos - 1;
        
        this->pos += dx;
        
        return this->stack[this->pos];
        
    }
    
};

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */
