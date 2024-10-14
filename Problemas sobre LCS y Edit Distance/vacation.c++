#include <iostream>
#include <vector>
#include <string>

using namespace std;

int lcs(const string& string1, const string& string2) {
    int len1 = string1.length() + 1;
    int len2 = string2.length() + 1;

    vector<vector<int>> matrix(len1, vector<int>(len2, 0));

    for (int i = 1; i < len1; i++) {
        for (int j = 1; j < len2; j++) {
            if (string1[i - 1] == string2[j - 1]) {
                matrix[i][j] = 1 + matrix[i - 1][j - 1];
            } else {
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1]);
            }
        }
    }

    return matrix[len1 - 1][len2 - 1];
}

int main() {
    string str1;
    int cases = 1;
    while (getline(cin, str1) && str1 != "#") {
        string str2;
        getline(cin, str2);
        cout << "Case #" << cases << ": you can visit at most " << lcs(str1, str2) << " cities." << endl;
        cases++;
    }
    return 0;
}