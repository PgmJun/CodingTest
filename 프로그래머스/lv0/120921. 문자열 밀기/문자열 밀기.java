class Solution {
   public static int solution(String A, String B) {
		int answer = 0;
		boolean success = false;
		int cnt = A.length();

		int rightResult = findRight(A, B, answer, success, cnt);
		if(rightResult != -1) {
			return rightResult;
		} else {
			return findLeft(A, B, answer, success, cnt);
		}
	}

	private static int findRight(String A, String B, int answer, boolean success, int cnt) {
		StringBuilder sb = new StringBuilder();
		for(int i = 0; i < cnt; i++) {
			sb.append((A.charAt(0)));
			sb.append(A.substring(1));
			A = sb.toString();
			if(A.equals(B)) {
				success = true;
				answer = i;
				break;
			}
			sb.setLength(0);
		}

		if(success) {
			return answer;
		}
		return -1;
	}

	private static int findLeft(String A, String B, int answer, boolean success, int cnt) {
		StringBuilder sb = new StringBuilder();

		for(int i = 0; i < cnt; i++) {
			if(A.equals(B)) {
				answer = i;
				success = true;
				break;
			}

			sb.setLength(0);
			sb.append((A.charAt(A.length()-1)));
			sb.append(A.substring(0,A.length()-1));
			A = sb.toString();
		}

		if(success) {
			return answer;
		}
		return -1;
	}
}