import java.util.HashSet;
import java.util.Arrays;
import java.util.Set;

class prob_349
{

  public static int[] intersection(int[] nums1, int[] nums2) {
      if(nums1.length ==0 || nums2.length ==0){
        return new int[] {} ;
      }
      Set<Integer> set1 = new HashSet<Integer>();
      for(Integer num : nums1){
        set1.add(num);
      }
      Set<Integer> set2 = new HashSet<Integer>();
      for(Integer num : nums2){
        set2.add(num);
      }
      System.out.println("set1 : "+set1);
      System.out.println("set2 : "+set2);

      //segue to new function for the sake of better complexity | taking short length as main iteration through but it done wothout it for now
      Set<Integer> temp = new HashSet<Integer>();

      if(set1.size() > set2.size()){
        temp = set2;
        set2 = set1;
        set1 = temp;
  
      }

      int[] outputArr = new int[set1.size()];
      int i =0;
      System.out.println("values inside outputArr are :");
      for(Integer num: set1){
        if(set2.contains(num)){
          outputArr[i++] = (int)num ;
          System.out.println("value : (int) "+ (int)num + " | (Integer) "+num );
        }
      }
      // return outputArr;
      return Arrays.copyOf(outputArr, i);
      // return new int[] {};
      // for(int n : outputArr){
      //   System.out.println(n);
      // }
  }
  public static void main(String[] args) {
    int num1[] = {};
    int num2[] = {2,2};

    intersection(num1,num2);
  }
}