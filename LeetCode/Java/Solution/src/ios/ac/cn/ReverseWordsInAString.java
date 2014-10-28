package ios.ac.cn;
public class ReverseWordsInAString {
	/**
	 * LeetCode: Reverse Words in a String 
	 * 
	 * 1. 分割字符串时，可能会分出空字符串，这些空串不应该放在最终结果中
	 * 2. 最终结果的末尾可能出现空格，由于无法判断最后一次非空字符串在哪里，也就
	 * 不能确定哪一个字符串后面不应该加空格，所以得到最终结果后，再去除最后的空格 
	 * 
	 * @param s
	 * @return
	 */
	public String reverseWords(String s) {
		String[] words = s.split(" ");
		StringBuffer buffer = new StringBuffer();
		for (int i = words.length - 1; i >= 0; i--) {
			if (words[i].length() > 0) {
				buffer.append(words[i]);
				buffer.append(" ");
			}
		}
		return buffer.toString().trim();
	}

	public static void main(String[] args) {
		ReverseWordsInAString s = new ReverseWordsInAString();
		System.out.println(s.reverseWords(" "));
		System.out.println(s.reverseWords("the sky is blue"));
		System.out.println(s.reverseWords("1 "));
		System.out.println("   ".split(" ").length);
		System.out.println("  1  ".split(" ").length);
	}
}
