
public class Tester
{
    
    public Tester()
    {
        stringYak("yakpak");
    }

    public String stringYak(String str) {
      String result = "";
      
      for (int i=0; i<str.length(); i++) {
        // Look for i starting a "yak" -- advance i in that case
        if (i+2<str.length() && str.charAt(i)=='y' && str.charAt(i+2)=='k') {
          i =  i + 2;
        } else { // Otherwise do the normal append
          result = result + str.charAt(i);
        }
      }
      
      return result;
    }

}
