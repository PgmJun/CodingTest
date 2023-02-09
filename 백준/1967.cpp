#include <bits/stdc++.h>
using namespace std;

const int N = 100005;
vector<pair<int, int>> graph[N];
bool visited[N];
int result;

void dfs(int node, int length, int maxLength) {
    maxLength = max(maxLength, length);
    result = max(result, maxLength);
    for (int i = 0; i < graph[node].size(); i++) {
        int n = graph[node][i].first, l = graph[node][i].second;
        if (!visited[n]) {
            visited[n] = true;
            dfs(n, l + length, maxLength);
        }
    }
}

int main() {
    int n;
    cin >> n;

    for (int i = 1; i < n; i++) {
        int s, g, l;
        cin >> s >> g >> l;
        graph[s].push_back(make_pair(g, l));
        graph[g].push_back(make_pair(s, l));
    }

    for (int i = 1; i <= n; i++) {
        memset(visited, false, sizeof(visited));
        visited[i] = true;
        dfs(i, 0, -1);
    }

    cout << result << endl;
    return 0;
}