import re

input_file = open("day04_input.txt", 'r')
inputs = input_file.read().split("\n\n")

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional = "cid"

pt1_count = 0
pt2_count = 0
for passport in inputs:
    fields = re.split('\n| ', passport)
    keys = [fields[i][:fields[i].index(':')] for i in range(len(fields))]
    vals = [fields[i][fields[i].index(':')+1:] for i in range(len(fields))]
    
    pass_dict = {}
    for i in range(len(keys)):
        pass_dict[keys[i]] = vals[i]

    pt1_valid = True
    for field in required_fields:
        if field not in keys:
            pt1_valid = False
            break
    if pt1_valid:
        pt1_count += 1


    if "byr" not in pass_dict or (int(pass_dict["byr"]) < 1920 or 2020 < int(pass_dict["byr"])):
        continue
    if "iyr" not in pass_dict or (int(pass_dict["iyr"]) < 2010 or 2020 < int(pass_dict["iyr"])):
        continue
    if "eyr" not in pass_dict or (len(pass_dict["eyr"]) < 4 or int(pass_dict["eyr"]) < 2020 or 2030 < int(pass_dict["eyr"])):
        continue
    if "hgt" not in pass_dict or not pass_dict["hgt"][:-2].isnumeric() or not (pass_dict["hgt"][-2:] == "cm" or pass_dict["hgt"][-2:] == "in"):
        continue
    elif pass_dict["hgt"][-2:] == "cm" and (int(pass_dict["hgt"][:-2]) < 150 or 193 < int(pass_dict["hgt"][:-2])):
        continue
    elif pass_dict["hgt"][-2:] == "in" and (int(pass_dict["hgt"][:-2]) < 59 or 76 < int(pass_dict["hgt"][:-2])):
        continue
    if "hcl" not in pass_dict or pass_dict["hcl"][0] != "#" or len(pass_dict["hcl"]) != 7:
        continue
    elif sum([1 if x in '0123456789abcdef' else 0 for x in pass_dict['hcl'][1:]]) != 6:
        continue
    if "ecl" not in pass_dict or pass_dict["ecl"] not in ["amb","blu","brn","gry","grn","hzl","oth"]:
        continue
    if "pid" not in pass_dict or len(pass_dict["pid"]) != 9 or not pass_dict["pid"].isnumeric():
        continue
    
    pt2_count += 1



print(pt1_count)
print(pt2_count)