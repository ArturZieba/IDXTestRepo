// Source: https://leetcode.com/problems/leaf-similar-trees/description/?envType=study-plan-v2&envId=leetcode-75

#include <iostream>

struct TreeNode 
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

bool leafSimilar(TreeNode* root1, TreeNode* root2) 
{
    return false;
}

int main()
{
    /*
    root01 = [3,5,1,6,2,9,8,null,null,7,4];
    root02 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8];
    // Expected Output: true

    root11 = [1,2,3];
    root12 = [1,3,2];
    // Expected Output: false
    */
}