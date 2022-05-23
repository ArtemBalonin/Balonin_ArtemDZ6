
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    requests_list = []
    for line in f:
        remote_addr = line[:line.find(' ')]
        requests_type = line[line.find('"') + 1:line.find('"') + 4]
        requests_resource = line[line.find('/d'):line.find('HTTP')-1]
        tutle_requests = (remote_addr, requests_type, requests_resource)
        requests_list.append(tutle_requests)
        print(tutle_requests)
