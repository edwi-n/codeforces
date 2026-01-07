#include "bits/stdc++.h"

using namespace std;

// clang-format off
#define ll long long
#define ld long double
#define ull unsigned long long

#define sz(x) int((x).size())
#define all(x) begin(x), end(x)
#define F first
#define S second
#define pb push_back


//Debug Template
template<typename A, typename B> ostream& operator<<(ostream &os, const pair<A, B> &p) { return os << '(' << p.first << ", " << p.second << ')'; }
template<typename T_container, typename T = typename enable_if<!is_same<T_container, string>::value, typename T_container::value_type>::type> ostream& operator<<(ostream &os, const T_container &v) { os << '{'; string sep; for (const T &x : v) os << sep << x, sep = ", "; return os << '}'; }
 
void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }
#ifdef LOCAL
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif

// Custom hash map
struct custom_hash
{
    static uint64_t splitmix64(uint64_t x)
    {
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }
    size_t operator()(uint64_t x) const
    {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};
template <typename T1, typename T2> // Key should be integer type
using safe_map = unordered_map<T1, T2, custom_hash>;
 
// Operator overloads
template<typename T1, typename T2> // cin >> pair<T1, T2>
istream& operator>>(istream &istream, pair<T1, T2> &p) { return (istream >> p.first >> p.second); }
 
template<typename T> // cin >> vector<T>
istream& operator>>(istream &istream, vector<T> &v)
{
          for (auto &it : v)
                    cin >> it;
          return istream;
}
 
const int dx[4] = {1, 0, -1, 0}, dy[4] = {0, 1, 0, -1};
constexpr ll INF = 2e18;
constexpr ld EPS = 1e-9;
constexpr ll MOD = 998244353 ;//1e9 + 7;

#define endl '\n'

/* stuff you should look for
          * int overflow, array bounds
          * special cases (n=1?)
          * do smth instead of nothing and stay organized
          * WRITE STUFF DOWN
          * DON'T GET STUCK ON ONE APPROACH
    * remove certain headers (define int ll, define endl)
*/
// clang-format on

void solve();

int32_t main()
{
          ios_base::sync_with_stdio(0);
          cin.tie(0);
          cout << setprecision(15);
          int testCases = 1;
          cin >> testCases;
          while (testCases--)
          {
                    solve();
          }
          return 0;
}
void solve()
{
          int n;
          cin >> n;
          vector<int> arr(n);
          cin >> arr;
          if (arr[0] == arr[n - 1] && arr[0] == 0)
          {
                    cout << "Bob\n";
          }
          else
          {
                    cout << "Alice\n";
          }
}
