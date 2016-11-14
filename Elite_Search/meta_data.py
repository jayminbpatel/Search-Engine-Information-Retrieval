try:
    st = os.stat(n.url)
    print st[uid]
    data['size'] = st[ST_SIZE]
    print st[ST_SIZE]
except (ImportError, KeyError):
    print "fail"
