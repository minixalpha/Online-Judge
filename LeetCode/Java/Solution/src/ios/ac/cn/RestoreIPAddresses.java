package ios.ac.cn;

import java.util.ArrayList;
import java.util.List;

public class RestoreIPAddresses {
	/* ip 地址的字段不能大于 255, 长度大于1时，不能以0开始 */
	public List<String> restoreIpAddresses(String s) {
		return restoreIpAddresses(s, 1);
	}

	private List<String> restoreIpAddresses(String s, int seq) {
		List<String> ipList = new ArrayList<>();
		int len = s.length();
		if (seq < 4) {
			for (int i = 1; i <= 3 && i <= len; i++) {
				String head = s.substring(0, i);
				if (Integer.valueOf(head) > 255) {
					break;
				}
				List<String> subIPList = restoreIpAddresses(s.substring(i),
						seq + 1);
				for (String ip : subIPList) {
					ipList.add(head + "." + ip);
				}
				if (head.startsWith("0")) {
					break;
				}
			}
		} else {
			if (!(len > 3 || len < 1 || Integer.valueOf(s) > 255)) {
				if (!(len > 1 && s.startsWith("0"))) {
					ipList.add(s);
				}
			}
		}
		return ipList;
	}

	public static void main(String[] args) {
		for (String ip : new RestoreIPAddresses()
				.restoreIpAddresses("25525511135")) {
			System.out.println(ip);
		}
	}
}
