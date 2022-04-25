INCLUDE_UNSUBMITTED = False

csv = open('nio-module-list.csv', 'r')
module_dict = {}
module_map = {}
lines = csv.readlines()
for line in lines:
    x = [y.strip() for y in line.split(",")]
    idm = x[0]
    module = x[1] + "," + x[2] + "," + x[3]
    module_map[module] = idm
    module_dict[idm] = [0, 0, 0, 0, 0, 0]

csv = open('nio-status.csv', 'r')
lines = csv.readlines()[1:]
for line in lines:
    x = line.split(",")
    x = [y.strip() for y in x]
    # print(x)
    module = module_map[x[0]+","+x[1]+","+x[2]]
    module_dict[module][4] = module_dict[module][4] + 1
    '''
    if x[5] != "":
        module_dict[module][1] = module_dict[module][1] + 1
        num_fix = num_fix + 1
    '''
    # if x[7] != "":
    #     module_dict[module][0] = module_dict[module][0] + 1
    if INCLUDE_UNSUBMITTED:
        if x[6] == "Accepted" or x[6] == "Pending" or x[6] == "Rejected" or x[6] == "Opened":
            module_dict[module][1] =  module_dict[module][1] + 1
    else:
        if x[6] == "Accepted" or x[6] == "Rejected" or x[6] == "Opened":
            module_dict[module][1] =  module_dict[module][1] + 1
    if x[6] == "Accepted":
        module_dict[module][2] = module_dict[module][2] + 1
    if x[6] == "Deleted" or x[6] == "Deleted/Skipped" or x[6] == "Skipped" or x[6] == "DeveloperFixed":
        module_dict[module][3] = module_dict[module][3] + 1
    if x[6] == "Rejected":
        module_dict[module][5] = module_dict[module][5] + 1

total = [0, 0, 0, 0, 0, 0]
at_least_one_fix = 0
not_available = 0
for i in range(1, 35):
    module = "M" + str(i)
    if module_dict[module][1] > 0:
        at_least_one_fix = at_least_one_fix + 1
    if module_dict[module][4] == module_dict[module][3]:
        not_available  = not_available + 1
    print(module + " & "+ str(module_dict[module][4]) + " & " + str(module_dict[module][3]) + " & " + (str(module_dict[module][1]) if (module_dict[module][4] > module_dict[module][3]) else "N/A") + " & " + str(module_dict[module][2]) + " & " + str(module_dict[module][5]) + " \\\\")
    for j in range(0, 6):
        total[j] = total[j] + module_dict[module][j]

print("\\hline")
print("\\textbf{Total} & \\textbf{" + str(total[4]) + "} & \\textbf{" + str(total[3]) + "} & \\textbf{" + str(total[1]) + "} & \\textbf{" + str(total[2]) + "} & \\textbf{" + str(total[5]) + "}")
print("34 modules, " + str(at_least_one_fix) + " have at least one fix, " + str(not_available) + " not available")
