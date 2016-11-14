import json
with open('store.json', mode='a') as f:
        data['filename'] = n.url
        data['hash'] = get_hash(n.url)
        html = read_html(n.url)
        write_html(html, str(get_hash(n.url)))
        print "Writing : " + n.url
        json.dump(data, f)