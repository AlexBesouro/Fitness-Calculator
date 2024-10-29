from configparser import ConfigParser

def config(filename, section):
    # Create a parser
    parser = ConfigParser()
    parser.read(filename)
    # print(parser)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        # print(params)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f"Section {section} is not found in the {filename} file")

    return db

# print(config("food_database.ini", "postgresql"))