import func
import groups
import ruleproviders

    
head = [
    "mix-port: 9001\n",
    "allow-lan: true\n",
    "bind-address: '*'\n",
    "mode: rule\n",
    "log-level: info\n",
    "external-controller: '127.0.0.1:9002'\n",
    "ipv6: false\n",
    "tcp-concurrent: true\n",
    "tcp-fast-open: true\n",
    "network-buffer: 10240\n",
    "redir-port: 9003\n",
    "global-client-fingerprint: random\n",
]

dns = [
    "dns:\n",
    "  enable: false\n"
]


if __name__ == "__main__":
    proxies = func.download("https://substore.vansoursheng.top/substore/download/collection/vansour?target=ClashMeta")
    proxy_groups = ["proxy-groups:"]
    proxy_groups.extend(groups.main())
    rule_providers = ["rule-providers:"]
    rule_providers.append("  Youtube: { type: http, behavior: domain, url: 'https://gitee.com/vansour/ruleproviders/raw/main/youtube.txt',path: ./ruleset/youtube.yaml, interval: 86400 }")
    rule_providers.append("  Apple: { type: http, behavior: domain, url: 'https://gitee.com/vansour/ruleproviders/raw/main/apple.txt',path: ./ruleset/apple.yaml, interval: 86400 }")
    rule_providers.append("  CN: { type: http, behavior: domain, url: 'https://gitee.com/vansour/ruleproviders/raw/main/cn.txt',path: ./ruleset/cn.yaml, interval: 86400 }")
    rule_providers.append("  HK: { type: http, behavior: ipcidr, url: 'https://gitee.com/vansour/ruleproviders/raw/main/hk.txt',path: ./ruleset/hk.yaml, interval: 86400 }")

    rules = ["rules:"]
    rules.append("  - \'RULE-SET,Youtube,Youtube\'")
    rules.append("  - \'RULE-SET,HK,HK\'")
    rules.append("  - \'RULE-SET,CN,DIRECT\'")
    rules.append("  - \'MATCH,MainNode\'")
    with open("clash.yaml", "w", encoding="utf-8") as file:
        file.writelines(head)
        file.writelines(dns)
        for proxy in proxies:
            file.writelines(proxy + "\n")
        for proxy_group in proxy_groups:
            file.writelines(proxy_group + "\n")
        for rule_provider in rule_providers:
            file.writelines(rule_provider + "\n")
        for rule in rules:
            file.writelines(rule + "\n")
    
    ruleproviders.main()