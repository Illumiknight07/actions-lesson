from tree import Tree


class TreeImplementation(Tree):
    # Insert a value into the tree. Does nothing if the value is already in the tree.
    def insert(self, value: int) -> None:
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = TreeImplementation(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = TreeImplementation(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    # Check if the tree contains a value.
    def contains(self, value: int) -> bool:
        if value < self.value:
            if self.left is None:
                return False
            return self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            return self.right.contains(value)
        else:
            return True

    #  Remove a value from the tree. Raises a KeyError if the value is not
    #  in the tree, or a ValueError if the removal would result in an empty tree.
    def remove(self, value: int) -> None:
        self.only_one()

        if value < self.value:
            if self.left is None:
                raise KeyError("Value not in tree")
            self.left = self.left.remove(value)
        elif value > self.value:
            if self.right is None:
                raise KeyError("Value not in tree")
            self.right = self.right.remove(value)

    # Checks if there is only one thing in the tree and then raises a ValueError
    def only_one(self) -> None:
        if self.left is None and self.right is None:
            raise ValueError("Cannot remove last value in tree")

    # Return the minimum value in the tree.
    def min_value(self) -> int:
        if self.left is None:
            return self.value
        return self.left.min_value()

    # Return the maximum value in the tree.
    def max_value(self) -> int:
        if self.right is None:
            return self.value
        return self.right.max_value()

    # Return the inorder traversal (left, root, right) of the tree as a list.
    def inorder_traversal(self) -> list[int]:
        result = []
        if self.left is not None:
            result.extend(self.left.inorder_traversal())
        result.append(self.value)
        if self.right is not None:
            result.extend(self.right.inorder_traversal())
        return result
