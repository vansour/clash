import func
def main():
	names = func.json2name()
	proxy_groups = []
	proxy_groups_youtube = []
	for name in names:
		if name.find("主用 02 香港") != -1:
			proxy_groups_youtube.append(name + ", ")
	tmp_proxy_group = "  - { name: 'Youtube', type: load-balance, proxies: ["
	for proxy_youtube in proxy_groups_youtube:
		tmp_proxy_group += proxy_youtube
	tmp_proxy_group += "], url: 'https://www.google.com/generate_204', interval: 300, tolerance: 50, strategy: round-robin }"
	proxy_groups.append(tmp_proxy_group)
	proxy_groups_main = []
	for name in names:
		proxy_groups_main.append(name + ", ")
	tmp_proxy_group = "  - { name: 'MainNode', type: select, proxies: ["
	for proxy_main in proxy_groups_main:
		tmp_proxy_group += proxy_main
	tmp_proxy_group += "] }"
	proxy_groups.append(tmp_proxy_group)
	return proxy_groups
	

	