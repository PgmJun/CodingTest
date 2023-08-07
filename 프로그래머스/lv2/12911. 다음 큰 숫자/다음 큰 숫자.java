class Solution {
    static int answer = 0;
	public static int solution(int n) {
		int nBitCount = Integer.bitCount(n);
		int i = n;

		while(true) {
			i++;
			if(nBitCount == Integer.bitCount(i)) {
				answer = i;
				break;
			}
		}
		return answer;
	}
}