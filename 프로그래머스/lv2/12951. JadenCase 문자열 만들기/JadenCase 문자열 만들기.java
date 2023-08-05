import java.util.StringJoiner;

class Solution {
    static final String BLANK = " ";

	static int charInTextCount = 0;
	static StringBuilder sb = new StringBuilder();
	static String[] splitTexts;
	public static String solution(String s) {

		splitTexts = s.split(BLANK);

		for (int i = 0; i < splitTexts.length; i++) {

			if(splitTexts[i].equals("")) {
				sb.append(BLANK);
				charInTextCount++;
			} else {
				String text = formatJadenCase(splitTexts[i]);
				charInTextCount+=text.length();
				sb.append(text);
				spacingIsNotLastText(i);
			}
		}
		addAfterSpace(s);

		return sb.toString();
	}

	private static void addAfterSpace(String s) {
		int afterSpaceCount = getAfterSpaceCount(sb.toString(), s);
		for(int i = 0; i < afterSpaceCount; i++) {
			sb.append(" ");
		}
	}

	private static void spacingIsNotLastText(int i) {
		if(i != splitTexts.length-1) {
			sb.append(BLANK);
		}
	}

	private static int getAfterSpaceCount(String after, String before) {
		return before.length() - after.length();
	}

	private static String formatJadenCase(String splitTexts) {
		return String.valueOf(splitTexts.charAt(0)).toUpperCase() + splitTexts.substring(1).toLowerCase();
	}
}