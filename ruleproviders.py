import func

def main():
	func.domain2rule("https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/refs/heads/sing/geo/geosite/youtube.json", "youtube.txt")
	func.domain2rule("https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/refs/heads/sing/geo/geosite/apple.json", "apple.txt")
	func.domain2rule("https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/refs/heads/sing/geo/geosite/cn.json", "cn.txt")
	func.ip2rule("https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/refs/heads/sing/geo/geoip/hk.json","hk.txt")