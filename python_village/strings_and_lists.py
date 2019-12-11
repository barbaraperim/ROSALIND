def string_slice(string):
    string_list = string.split()
    new_string = string_list[0]
    new_string = new_string[int(string_list[1]):int(string_list[2])+1] + " " + new_string[int(string_list[3]):int(string_list[4])+1]
    print(new_string)
    
string_slice("SUkEpB5jjyvfo7xkNFurciferyjvFLQCYKqCJFjWrs1wvqoqI3XJVmv1y50xHCk224zBo0zxrgkzvuHa5RQjv4IokhD0OjYCrleucopterahrYLCkZIGYh9AADaHrg06POi7lem7Aan3CrI2EmEsSCvO5F9ITXKS3N0ggpeom0rirYh.\n17 24 97 106")