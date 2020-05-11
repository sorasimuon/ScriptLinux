from subprocess import Popen, PIPE

def run_df(options):
    df = Popen(["df", "-h"], stdout=PIPE)
    list_fs = {}
    for bytes in df.stdout:
        line = bytes.decode()

        # get the header
        if line.startswith("filesystem"):
            header = line

        if line.startswith("/dev/sd"):
            fs_line = line.split()
            list_fs[fs_line[0]] = int(fs_line[4][:-1])

    # Print the result to stdout
    print(header)
    for k,v in list_fs.items():
        if v > options.threshold:
            print("CRITICAL >> {} is {}% full.".format(k,v))






