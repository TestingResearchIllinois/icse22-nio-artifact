with open("nio-status.csv", "r") as fin:
    lines = fin.readlines()
    only_nio = 0
    only_victim = 3168 # wc -l known-victims-py.csv
    detected_both = 0
    fixed_only_nio = 0
    fixed_both = 0
    for i in range(1, len(lines)):
        line = lines[i].strip()
        test = line.split(",")[2]
        victim_status = line.split(",")[3]
        if victim_status == "yes":
            only_victim -= 1
            detected_both += 1
        else:
            assert victim_status == "no"
            only_nio += 1
        pr_link = line.split(",")[4]
        if "http" in pr_link and not "InspiredAFix" in line.split(",")[5]: # fixed tests
            if victim_status == "yes":
                fixed_both += 1
            else:
                fixed_only_nio += 1
    print("======== Generating Figure 6 all tests Venn diagram")
    print("only_nio", only_nio)
    print("only_victim", only_victim)
    print("detected_both", detected_both)
    print("======== Generating Figure 6 fixed tests Venn diagram")
    print("fixed_only_nio", fixed_only_nio)
    print("fixed_both", fixed_both)
