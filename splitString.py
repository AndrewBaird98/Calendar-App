import re
import io


def main():

    with io.open("DummyData.txt", "r", newline=None) as fd:
        List = []
        for line in fd:

            line = line.rstrip()
            if len(line) > 0:
                print('\n')
                tokens = line.split('\";\"')[0].split('\"$\"')
                for x in tokens:
                    List.append(x)
                    print(x)


if __name__ == "__main__":
    main()
