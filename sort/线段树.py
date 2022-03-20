def build_tree(nums, tree, node, start, end):
    if start == end:
        tree[node] = nums[start]
        return None

    mid = (start + end) // 2
    left_child = 2 * node + 1
    right_child = 2 * node + 2
    build_tree(nums, tree, left_child, start, mid)
    build_tree(nums, tree, right_child, mid + 1, end)
    tree[node] = tree[left_child] + tree[right_child]
    return None


def update(nums, tree, node, start, end, idx, val):
    if start == end:
        nums[idx] = val
        tree[node] = val
        return None

    mid = (start + end) // 2
    left_child = 2 * node + 1
    right_child = 2 * node + 2

    # 要判断向左走还是向右走
    if idx > mid:
        # 往右边走
        update(nums, tree, right_child, mid + 1, end, idx, val)
    else:
        # 往左边走
        update(nums, tree, left_child, start, mid, idx, val)

    tree[node] = tree[left_child] + tree[right_child]
    return None


def query(nums, tree, node, start, end, left, right):
    # [left, right] 是要求和的区间
    # [start, end] 是tree中每一个节点对应的区间和
    if left > end or right < start: return 0
    elif left <= start and right >= end: return tree[node]
    elif start == end: return tree[node]

    mid = (start + end) // 2
    left_child = 2 * node + 1
    right_child = 2 * node + 2

    left_sum = query(nums, tree, left_child, start, mid, left, right)
    right_sum = query(nums, tree, right_child, mid + 1, end, left, right)

    return left_sum + right_sum




if __name__ == '__main__':
    nums = [1, 3, 5, 7, 9, 11]
    n = len(nums)
    tree = [0] * 15
    build_tree(nums, tree, 0, 0, n - 1)
    print(tree)
    print('\n')


    update(nums, tree, 0, 0, n - 1, 4, 2)
    print(nums)
    print(tree)

    # 最难写的其实是query

    print(query(nums, tree, 0, 0, n - 1, 2, 4))


