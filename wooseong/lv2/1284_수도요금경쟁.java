// 문제: 1284 수도 요금 경쟁
// 링크: https://swexpertacademy.com/main/code/problem/problemList.do (번호 1284 검색)
// 날짜: 2026-10-01
//
// [접근] A사 요금은 P*W, B사 요금은 W가 R 이하이면 기본요금 Q,
//        R을 넘으면 Q + (W-R)*S로 계산한 뒤 둘 중 작은 값을 출력한다.
// [시간복잡도] O(1) (테스트 케이스당)
// [메모] B사 초과 요금은 전체 사용량이 아니라 초과분(W-R)에만 S를 곱해야 함.
//        입력 순서는 P Q R S W.

import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();

		for (int test_case = 1; test_case <= T; test_case++)
		{
			int P = sc.nextInt();
			int Q = sc.nextInt();
			int R = sc.nextInt();
			int S = sc.nextInt();
			int W = sc.nextInt();

			int a = P * W;
			int b = Q;
			if (W > R) {
				b += (W - R) * S;
			}

			System.out.println("#" + test_case + " " + Math.min(a, b));
		}
	}
}
