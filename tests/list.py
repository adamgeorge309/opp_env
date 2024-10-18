def expand_project_filter(project_filter):
    cmd = f"opp_env list --flat | grep -P '{project_filter}'"
    print(cmd, end="")
    list = sorted(subprocess.check_output(cmd, shell=True, text=True).split())
    # print(list)
    # type(list)
    # print(" --> ", " ".join(list))
    return list

expand_project_filter()