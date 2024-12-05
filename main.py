

# learn about hashmap


def list_methods(list):
    print(list[-1], "From Last Index")
    print(len(list))

    for i in range(len(list)):
        print(i, "-------")
        return i

    return list


lists = ['11', '25', '30', '2']


lists_string = ["Eleven", "Twenty", "Thirty", "One", "Axios"]

sorted_list = lists_string.sort()


print(sorted_list, "Sorted------")

print(lists_string.sort(key=len, reverse=True), "string sorted")

list_methods(lists)


# thislist = list(("apple", "banana", "cherry"))


# print(type(thislist), "list:")
