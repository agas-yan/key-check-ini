with open('input.ini', 'r') as f:
    dup_key = []
    bucket = set()
    for line in f:
        tmp = line.strip()
        if tmp != '' and tmp.startswith('['):
            old_len = len(bucket)
            bucket.add(tmp)
            if old_len == len(bucket):
                dup_key.append(tmp)
# if dup_key > 0 print to new file
if len(dup_key) > 0:
    # new file
    with open('tmp.txt', 'w') as f:
        for i in dup_key:
            f.write(i + "\n")
else:
    print("no duplicated key")