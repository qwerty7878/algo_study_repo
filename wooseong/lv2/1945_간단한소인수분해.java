// 접근: 2, 3, 5, 7, 11 순서로 N을 나눌 수 있는 만큼 나누며 횟수를 센다.
// 시간복잡도: O(log N)
// 메모: 지수 a~e는 각 소수가 곱해진 횟수. 출력은 공백으로 구분.


import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		
		int[] primes = {2, 3, 5, 7, 11};
        
	for(int test_case = 1; test_case <= T; test_case++)
		{
		
		int N = sc.nextInt();

			StringBuilder sb = new StringBuilder();
			sb.append('#').append(test_case);

			for (int p : primes) {
				int cnt = 0;
				while (N % p == 0) {
					N /= p;
					cnt++;
		}
                sb.append(' ').append(cnt);
		}
            System.out.println(sb);
		}
	}
}
