def split_and_join(string):
    r = string.split()
    joined_string = "-".join(r)
    return joined_string

    if __name__ == '__main__':
        line = input()
        result = split_and_join(line)
        print(result)