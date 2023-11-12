class Solution {
public://use modified bfs
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        if(source == target) return 0;

        int n = routes.size();
        unordered_map<int, vector<int>> adj;//(bus stop, (bus no/ind))

        for(int i = 0; i < n; i++){
            for(auto &stop: routes[i]){
                adj[stop].push_back(i);
            }
        }

        vector<int> vis(501, 0);
        queue<int> q;
        for(auto &route: adj[source]){
            q.push(route);
            vis[route] = 1;
        }

        int cnt = 1;//for the source bus
        while(!q.empty()){
            int size = q.size();

            while(size--){
                int bus_no = q.front();
                q.pop();

                for(auto &stop: routes[bus_no]){
                    if(stop == target){
                        return cnt;
                    }
                    
                    for(auto &bus_stops: adj[stop]){
                        if(!vis[bus_stops]){
                            vis[bus_stops] = 1;
                            q.push(bus_stops);
                        }
                    }
                }
            }
            cnt++;
        }

        return -1;
    }
};
