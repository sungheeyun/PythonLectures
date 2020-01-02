import json


if __name__ == "__main__":

    with open("months.json") as fid:
        months_ = json.load(fid)

    months = dict()
    for key, value in months_.items():
        months[int(key)] = value

    print("The dictionary contains the following keys: ", months.keys())
    print("The dictionary contains the following keys: ", list(months.keys()))
    print(months[1])
    print(months.pop(5))
    print(months)
    months[5] = "MAY"
    print(months)
    print(list(months.keys()))

    months[1] = "Jan"
    print(months)

    print(sorted(months.keys()))
    print(months)

    for key in months:
        print(key, months[key])

    print("---- KEY/VALUE PAIR ----")
    for key, value in sorted(months.items()):
        print("months[", key, "] =",  value)
