# read top c++ answers posted on leetcode discussion for reference

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
 
// using stack, fake interator
class NestedIterator {
    
private:
    stack<NestedInteger> s;
    
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        int size = nestedList.size();
        for(int i = size - 1; i >= 0; i--){
            s.push(nestedList[i]);
        }
    }

    int next() {
        int result = s.top().getInteger();
        s.pop();
        return result;
    }

    bool hasNext() {
        while(!s.empty()){
            NestedInteger curr = s.top();
            if(curr.isInteger()) return true;
            s.pop();
            vector<NestedInteger> currlist = curr.getList();
            int size = currlist.size();
            for(int i = size - 1; i >= 0; i--){
                s.push(currlist[i]);
            }
        }
        return false;
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
 
 
// using stack, real iterator
 
class NestedIterator {

private:
    stack<vector<NestedInteger>::iterator> begins, ends;
    
public:
    NestedIterator(vector<NestedInteger> &nestedList){
        begins.push(nestedList.begin());
        ends.push(nestedList.end());
    }

    int next() {
        hasNext();
        return (begins.top()++)->getInteger();
    }

    bool hasNext() {
        while(begins.size()){
            if(begins.top() == ends.top()){
                begins.pop();
                ends.pop();
            } 
            else{
                auto x = begins.top();
                if(x->isInteger()) return true;
                begins.top()++;
                begins.push(x->getList().begin());
                ends.push(x->getList().end());
            }
        }
        return false;
    }
};
