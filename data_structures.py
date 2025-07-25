from typing import List

from data_structures.LinkedList import LinkedList, display, ListNode


def fold_linked_list(head: ListNode) -> ListNode:
    if not head:
        return head
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow
    while curr:  # while we have nodes to process, e.g. curr != None
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    first = head
    second = prev

    while second.next:
        # save the next nodes
        first_next = first.next
        second_next = second.next

        # insert the current node from 2 after the current node from 1
        second.next = first.next
        first.next = second

        # update pointers for next iteration
        first = first_next
        second = second_next
    return head


def reverse_linked_list(head: ListNode) -> ListNode:
    if not head:
        return head

    prev = None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev


def reverse_k_groups(head, k):
    dummy = ListNode(0)
    dummy.next = head
    ptr = dummy

    while ptr:
        # Keep track of the current position
        tracker = ptr
        # Traverse k nodes to check if there are enough nodes to reverse
        for _ in range(k):
            # If there are not enough nodes to reverse, break out of the loop
            if tracker == None:
                break
            tracker = tracker.next

        if tracker == None:
            break

        # Reverse the current group of k nodes
        previous = None
        current = ptr.next
        for _ in range(k):
            # temporarily store the next node
            next = current.next
            current.next = previous
            previous = current
            current = next

        # Connect the reversed group to the rest of the linked list
        last_node_of_reversed_group = ptr.next
        last_node_of_reversed_group.next = current
        ptr.next = previous
        ptr = last_node_of_reversed_group

    return dummy.next


def valid_parens(string: str) -> bool:
    stack = []
    parens = {"}": "{", ")": "(", "]": "["}

    for s in string:  # O(N)
        if s not in parens.keys():
            stack.append(s)
        else:
            if len(stack) == 0:
                return False
            curr_parens = stack.pop()
            if curr_parens != parens[s]:
                return False

    if len(stack) > 0:
        return False
    return True


def remove_duplicates(string: str) -> str:
    stack = []
    for s in string:
        if not stack:
            stack.append(s)
        else:
            last = stack[-1]
            if s == last:
                stack.pop()
            else:
                stack.append(s)
    return "".join(stack)


def calculator(expression: str) -> int:
    number = 0
    sign_value = 1
    result = 0
    operations_stack = []

    for c in expression:
        if c.isdigit():
            number = number * 10 + int(c)
        if c in "+-":
            result += number * sign_value
            sign_value = -1 if c == "-" else 1
            number = 0
        elif c == "(":
            operations_stack.append(result)
            operations_stack.append(sign_value)
            result = 0
            sign_value = 1

        elif c == ")":
            result += sign_value * number
            pop_sign_value = operations_stack.pop()
            result *= pop_sign_value

            second_value = operations_stack.pop()
            result += second_value
            number = 0

    return result + number * sign_value


def set_matrix_zeroes(mat: List[List[int]]) -> List[List[int]]:
    frow = fcol = False
    m = len(mat)
    n = len(mat[0])

    for i in range(m):
        for j in range(n):  # O(M x N)
            if mat[i][0] == 0:
                frow = True
            if mat[0][j] == 0:
                fcol = True

    for i in range(1, m):
        for j in range(1, n):
            if mat[i][j] == 0:
                mat[0][j] = 0
                mat[i][0] = 0

    for i in range(1, m):
        if mat[i][0] == 0:
            for j in range(1, n):
                mat[i][j] = 0

    for j in range(1, n):
        if mat[0][j] == 0:
            for i in range(1, m):
                mat[i][j] = 0

    if frow:
        for i in range(m):
            mat[i][0] = 0
    if fcol:
        for j in range(n):
            mat[0][j] = 0

    return mat


def rotate_image(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    if n < 2:
        return matrix

    for row in range(n - 1 // 2):  # O(N^2)
        for col in range(row, n - 1 - row):
            top_left = (row, col)
            top_right = (col, n - 1 - row)
            bottom_right = (n - 1 - row, n - 1 - col)
            bottom_left = (n - 1 - col, row)

            # swap top left and top right
            (matrix[top_left[0]][top_left[1]], matrix[top_right[0]][top_right[1]]) = (
                matrix[top_right[0]][top_right[1]],
                matrix[top_left[0]][top_left[1]],
            )
            # swap top left and bottom right
            (
                matrix[top_left[0]][top_left[1]],
                matrix[bottom_right[0]][bottom_right[1]],
            ) = (
                matrix[bottom_right[0]][bottom_right[1]],
                matrix[top_left[0]][top_left[1]],
            )
            # swap top left and bottom left
            (
                matrix[top_left[0]][top_left[1]],
                matrix[bottom_left[0]][bottom_left[1]],
            ) = (
                matrix[bottom_left[0]][bottom_left[1]],
                matrix[top_left[0]][top_left[1]],
            )
    return matrix


def spiral_order(matrix: List[List[int]]) -> List[int]:
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, -1
    direction = 1
    result = []

    while rows > 0 and cols > 0:  # O(M * N)
        for _ in range(cols):
            col += direction
            result.append(matrix[row][col])
        rows -= 1

        for _ in range(rows):
            row += direction
            result.append(matrix[row][col])
        cols -= 1

        direction *= -1

    return result


def find_exit_column(grid: List[List[int]]) -> List[int]:
    rows, cols = len(grid), len(grid[0])
    result = [0 for _ in range(cols)]

    col = 0

    while col < cols:
        curr_col = col
        for row in range(rows):
            if grid[row][curr_col] == -1:
                if curr_col == 0:
                    result[col] = -1
                    break
                else:
                    prev_col = curr_col - 1
                    if grid[row][prev_col] == 1:
                        result[col] = -1
                        break
                    else:
                        curr_col -= 1
            else:
                if curr_col == cols - 1:
                    result[col] = -1
                    break
                else:
                    next_col = curr_col + 1
                    if grid[row][next_col] == -1:
                        result[col] = -1
                        break
                    else:
                        curr_col += 1
        if result[col] != -1:
            result[col] = curr_col
        col += 1

    return result


# def find_exit_column(grid):
#     result = [-1] * len(grid[0])
#     for col in range(len(grid[0])):
#         current_col = col
#         for row in range(len(grid)):
#             next_col = current_col + grid[row][current_col]
#             if (
#                 next_col < 0
#                 or next_col > len(grid[0]) - 1
#                 or grid[row][current_col] != grid[row][next_col]
#             ):
#                 break
#             if row == len(grid) - 1:
#                 result[col] = next_col
#             current_col = next_col
#     return result


if __name__ == "__main__":
    linked_list = LinkedList([1, 2, 3, 4, 5])
    # display(reverse_k_groups(linked_list.head, 2))
    # print(calculator("12 - (6 + 2) + 5"))
    print(
        find_exit_column(
            [
                [1, 1, 1, -1, 1, 1],
                [-1, -1, 1, -1, -1, 1],
                [1, 1, 1, -1, 1, 1],
                [-1, -1, -1, 1, 1, -1],
            ]
        )
    )
