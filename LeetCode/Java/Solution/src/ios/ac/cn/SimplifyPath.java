package ios.ac.cn;

import java.util.LinkedList;

public class SimplifyPath {
	// 注意分割后目录为空的情况
	public String simplifyPath(String path) {
		String[] dirs = path.split("/");
		LinkedList<String> stack = new LinkedList<>();
		for (String dir : dirs) {
			if (dir.equals("..")) {
				if (stack.size() > 0)
					stack.removeLast();
			} else if (!dir.equals(".") && !dir.equals("")) {
				stack.add(dir);
			}
		}
		StringBuilder builder = new StringBuilder();
		for (String dir : stack) {
			if (dir.length() > 0) {
				builder.append("/");
				builder.append(dir);
			}
		}

		String simplyPath = builder.toString();
		if (simplyPath.length() <= 1) {
			return "/";
		} else {
			if (simplyPath.endsWith("/")) {
				return simplyPath.substring(0, simplyPath.length() - 1);
			} else {
				return simplyPath;
			}
		}
	}

	public static void main(String[] args) {
		System.out.println(new SimplifyPath().simplifyPath("/a/./b/../../c/"));
		System.out.println(new SimplifyPath().simplifyPath("/home/"));
		System.out.println(new SimplifyPath().simplifyPath("/"));
		System.out.println(new SimplifyPath().simplifyPath("/home/../../.."));
		System.out.println(new SimplifyPath().simplifyPath("/abc/..."));
	}
}
