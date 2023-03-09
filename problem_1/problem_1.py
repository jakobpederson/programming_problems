# Given coordinates, what is the largest rectangle that can be generated
# I think the idea is to take the biggest coordinates to generate the rectangle

coords = [(1, 2), (3, 4), (6, 5), (5, 3)]


# So the only x-coords we care about are the largest and the smallest, so 1 and 6
# The only y-coords we care about are the 2 and 5

x = sorted([_[0] for _ in coords])
y = sorted([_[1] for _ in coords])

smallest_x = x[0]
smallest_y = y[0]
largest_x = x[-1]
largest_y = y[-1]

answer = [(smallest_x, smallest_y), (smallest_x, largest_y), (largest_x, largest_y), (largest_x, smallest_y)]

min_x = coords[0][0]
min_y = coords[0][1]
max_x = coords[0][0]
max_y = coords[0][1]

# Can be done in O(n) by using a single for-loop
# for i in coords:
#     if min_x > i[0]:
#         min_x == i[0]
#     if max_x < i[0]:
#         max_x == i[0]
#     if min_y > i[1]:
#         min_y == i[1]
#     if max_y < i[1]:
#         max_y == i[1]
