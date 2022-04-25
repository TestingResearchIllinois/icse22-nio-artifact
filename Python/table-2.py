with open("nio-status.csv", "r") as f:
    lines = f.readlines()
    alls = len(lines) - 1
    cur_projectid = 0
    cur_sha = 0
    # detected, na, submitted, accepted, rejected, inspected
    cur_info = [0, 0, 0, 0, 0, 0]
    info = []
    for i in range(1, len(lines)):
        line = lines[i].strip()
        slug, sha, test, victim, link, status = line.split(",")
        if sha != cur_sha:
            if i != 1:
                info.append(["P" + str(cur_projectid)] + list(map(str, cur_info)))
                cur_info = [0, 0, 0, 0, 0, 0]
            cur_projectid += 1
            cur_sha = sha
        cur_info[0] += 1
        if "N/A" in status or "InspiredAFix" in status:
            cur_info[1] += 1
        elif link.startswith("http"):
            cur_info[2] += 1
            if "Accept" in status:
                cur_info[3] += 1
            if "Reject" in status:
                cur_info[4] += 1
        if len(status) != 0:
            cur_info[5] += 1
    info.append(["P" + str(cur_projectid)] + list(map(str, cur_info)))
    print("PID,Detected,N/A,Submitted,Accepted,Rejected")
    total = [0, 0, 0, 0, 0, 0]
    def print_each(item):
        if item[1] == item[2]: # Detected == N/A
            item[3] = "N/A"
        print(",".join(item[:-1]))
    for each in info:
        for i in range(1, len(each)):
            total[i-1] += int(each[i])
        print_each(each)

    print("Total,"+ ",".join(map(str, total[:-1])))
