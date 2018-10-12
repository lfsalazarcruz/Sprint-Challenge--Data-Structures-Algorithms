class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    cb(self.value)
    if self.left: # callback on left side of tree
      self.left.depth_first_for_each(cb)
    if self.right: # callback on right side of tree
      self.right.depth_first_for_each(cb) 

  def breadth_first_for_each(self, cb):
    # queue
    arr = []
    arr.append(self)
    while len(arr) > 0:
      cur_node = arr[0] # root
      if cur_node.left:
        arr.append(cur_node.left) # appending nodes on the left side to the array
      if cur_node.right:
        arr.append(cur_node.right) # appending nodes on the right side to the array
      arr.pop(0)
      cb(cur_node.value)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value



"""Recursive Implementation"""
  # def depth_first_for_each(self, cb):
  #   cb(self.value)
  #   if self.left:
  #     self.left.depth_first_for_each(cb)
  #   if self.right:
  #     self.right.depth_first_for_each(cb)

"""Iterative Implementation"""
  # def depth_first_for_each(self, cb):
  #   stack = []
  #   stack.append(self)

  #   while len(stack):
  #     current_node = stack.pop()
  #     if current_node.right:
  #       stack.append(current_node.right)
  #     if current_node.left:
  #       stack.append(current_node.left)
  #     cb(current_node.value)