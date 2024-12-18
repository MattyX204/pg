import sys

def read_data(file_name):
    data = []
    fp = open(file_name, "r")
    for line in fp:
        data.append(line.strip().split(","))
    return data
        
def write_data(file_name, data):
    with open(file_name, "w") as fp:
        for row in data:
            line = ",".join(row) + "\n"
            fp.write(line)


if __name__ == "__main__":
    try:
        file = sys.argv[1]
        data = read_data(file)
        print(data)

        write_data("excel3.csv,data")


        text = "Alice,Bob,Tomas"
        split_text = text.split(",")
        print(split_text)

        joined_text = ",".join(split_text)
        print(joined_text)


    except IndexError:
        print("Nejsou zadany zadne soubory")
    except FileNotFoundError:
        print("soubor neexistuje")

    