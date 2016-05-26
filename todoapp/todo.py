filename = "todo_data.txt"
data_separator = "|"


def read_file():
    file = open(filename, "r")
    lines = file.readlines()
    data = []

    for line in lines:
        data.append(line.rstrip('\n').split(data_separator))

    file.close()

    return data


def write_file(data):
    file = open(filename, "w")
    for d in data:
        file.write(d[0] + "|" + d[1] + "\n")
    file.close()

    return True


def todo_list(data):
    print("You saved the following to-do items:")

    for index, d in enumerate(data):
        if d[0] == "m":
            status = "x"
        else:
            status = " "

        print(str(index+1) + ". [" + status + "] " + d[1])


def todo_add(data):
    todo = input("Add an item: ")

    data.append(["u", todo])
    print("Item added.")

    return data


def todo_mark(data):
    try:
        answer = int(input("Which one do you want to mark as completed: "))
        data[answer-1][0] = "m"
        print(data[int(answer)-1][1] + " is completed")
    except ValueError:
        print("Oops, that's not a valid number")
        return
    except IndexError:
        print("Oops, there's no todo with that id")
    return data


def todo_archive(data):
    for index, d in enumerate(data):
        if d[0] == "m":
            del data[index]

    print("All completed tasks got deleted.")

    return data


def main():
    data = read_file()

    while True:
        answer = input(
            "Please specify a command [list, add, mark, archive, quit]: "
        )

        if answer == "list":
            todo_list(data)
        elif answer == "add":
            todo_add(data)
        elif answer == "mark":
            todo_mark(data)
        elif answer == "archive":
            todo_archive(data)
        elif answer == "quit":
            write_file(data)
            exit()
main()
