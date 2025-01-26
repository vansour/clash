import requests
import json

def download(url: str) -> list:
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查HTTP响应状态
        lines = []
        for line in response.iter_lines(decode_unicode=True):  # 逐行读取，保留行首空格
            lines.append(line)
        return lines
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        return []


def in_file( lines, filename ):
    with open(f"{filename}", 'w', encoding = 'utf-8') as f:
        for line in lines:
            f.writelines(line + "\n")
            
def domain2rule( url: str, filename: str ):
    tmp = download(url)
    in_file(tmp, ".tmp.json")
    with open(".tmp.json", "r", encoding = "utf-8") as file:
        data = json.load(file)
        tmp_rules = data.get("rules", [])
        rules = []
        for tmp_rule in tmp_rules:
            domains = tmp_rule.get("domain", "")
            domain_suffixs = tmp_rule.get("domain_suffix", "")
            for domain in domains:
                domain = "  - \'" + domain + "\'"
                rules.append(domain)
            
            for domain_suffix in domain_suffixs:
                domain_suffix = "  - \'+." + domain_suffix + "\'"
                rules.append(domain_suffix)
        
        rules = ["payload:"] + rules
            
    in_file(rules, filename)


def ip2rule( url: str, filename: str ):
    tmp = download(url)
    in_file(tmp, ".tmp.json")
    with open(".tmp.json", "r", encoding = "utf-8") as file:
        data = json.load(file)
        tmp_rules = data.get("rules", [])
        rules = []
        for tmp_rule in tmp_rules:
            ip_cidrs = tmp_rule.get("ip_cidr", "")
            for ip_cidr in ip_cidrs:
                ip_cidr = "  - \'" + ip_cidr + "\'"
                rules.append(ip_cidr)
        
        rules = ["payload:"] + rules
    
    in_file(rules, filename)
    
def json2name():
    proxies_jsons = download("https://substore.vansoursheng.top/substore/download/collection/vansour?target=JSON")
    proxies_jsons = ["{"] + ["\"proxies\": "] + proxies_jsons + ["}"]
    in_file(proxies_jsons, ".tmp.json")
    names = []
    with open(".tmp.json", "r", encoding = "utf-8") as file:
        data = json.load(file)
        proxies = data.get("proxies", [])
        for proxy in proxies:
            names.append(proxy.get("name", ""))
    return names
        
        
    




