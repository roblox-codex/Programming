class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        map<string, string> owners;
        map<string, string> parents;
        map<string, set<string>> unions;
        
        for(int i = 0; i < accounts.size(); i++){
            for(int j = 1; j < accounts[i].size(); j++){
                parents[accounts[i][j]] = accounts[i][j];
                owners[accounts[i][j]] = accounts[i][0];
            }
        }
        
        for(int i = 0; i < accounts.size(); i++){
            string topRoot = find(accounts[i][1], parents);
            for(int j = 2; j < accounts[i].size(); j++)
                parents[find(accounts[i][j], parents)] = topRoot;
        }
        
        for(int i = 0; i < accounts.size(); i++){
            for(int j = 1; j < accounts[i].size(); j++)
                unions[find(accounts[i][j], parents)].insert(accounts[i][j]);
        }
        
        vector<vector<string>> result;
        for(auto const &emails : unions){
            vector<string> e(emails.second.begin(), emails.second.end());
            e.insert(e.begin(), owners[emails.first]);
            result.push_back(e);
        }
        
        return result;
    }

private:
    string find(string s, map<string, string> &p){
        if(s != p[s]) 
            p[s] = find(p[s], p);
        return p[s];
    }
};
