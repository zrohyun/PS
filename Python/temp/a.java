import java.io.*;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.TreeSet;

class Main {
	public static int cntPrimeNum = 0;    // 오른쪽 절단 소수 카운트
  public static TreeSet<Integer> setPrimeNum = null;    // 소수를 담을 집합
  public static boolean bRightCuttingPrimeNum = true;    // 소수판단 플래그
  public static int digitCnt = 0;        // 검사 자리수 
	public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(System.in);
        
        long begin = System.currentTimeMillis();
        
        // 자리수 설정
        digitCnt = scanner.nextInt();
        
        // 소수를 담을 집합 할당
        setPrimeNum = new TreeSet<Integer>();
    
         // 오른쪽 절단 소수를 구함.
         // 자리수가 1인 경우에는 소수가 2, 3, 5, 7 임.
        int curDigit = 1;
        getPrimeNumber(2, curDigit);
        getPrimeNumber(3, curDigit);
        getPrimeNumber(5, curDigit);
        getPrimeNumber(7, curDigit);
        
        // 집합의 내용을 스트링으로 받아서 출력포맷으로 변경
        // [1, 2, 3] ==> 1 2 3
				

        String nums = setPrimeNum.toString();
        nums = nums.substring(1, nums.length()-1);
        nums = nums.replace(", ", " ");
        
        // 결과 출력
        System.out.println(nums);
        
        long end = System.currentTimeMillis();
        
        scanner.close();
    }
	private static void getPrimeNumber(int curNum, int curDigit) {
        
        // 현재자리수가 주어진 자리수보다 크면 종료
        if(curDigit > digitCnt) {
            return;
        }
        
        // 현재 수가 소수가 아니면 종료
        if(!isPrimeNumber(curNum)) {
            return;
        }
        
        // 소수이고 두자리 이상이면 저장
        if(curNum > Math.pow(10, digitCnt-1)) {
            setPrimeNum.add(curNum);
            cntPrimeNum++;
        }
        
        // 현재 소수숫자에 10을 곱하고 끝자리에 1, 3, 7, 9를 더하고,
        // 자리수를 증가시켜서 재귀호출
        getPrimeNumber(curNum*10 + 1, curDigit + 1);
        getPrimeNumber(curNum*10 + 3,  curDigit + 1);
        getPrimeNumber(curNum*10 + 7, curDigit + 1);
        getPrimeNumber(curNum*10 + 9, curDigit + 1);
    }
 
    private static boolean isPrimeNumber(int num) {
        boolean ret = true;
        int mokCnt = 0;
        
        // 1은 소수가 아님.
        if(num == 1) {
            return false;
        }
        
        for (int i = 1; i <= num; i++) {
            if(num % i == 0) {
                mokCnt++;
                // 소수는 1과 자기자신이 약수이기 때문에
                // 목 카운트가 2보다 크면 소수가 아님.
                 if(mokCnt > 2) {
                    ret = false;
                    break;
                }
            }
        }
        
        return ret;
    }


}