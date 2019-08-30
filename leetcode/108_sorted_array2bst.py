from utils import TreeNode, inorder_traversal


def sorted_array2bst(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array2bst(nums[:mid])
    root.right = sorted_array2bst(nums[mid+1:])
    return root


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    print(inorder_traversal(sorted_array2bst(nums)))
