import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


def common_member(a, b):
    # initialize set a
    a_set = set(a)
    # initialize set b
    b_set = set(b)
    # if commonality exists in set a and set b
    # put coherce data type to list and print
    # print length to make sure it is same duplicates as first example (non-optimized)
    if a_set & b_set:
        print(list(a_set & b_set))
        print(len(list(a_set & b_set)))


common_member(names_1, names_2)

# original end time, 6 seconds-ish
# optimized run time, .007 seconds-ish
end_time = time.time()
# print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
