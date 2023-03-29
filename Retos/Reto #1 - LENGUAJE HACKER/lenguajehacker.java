import java.util.HashMap;
import java.util.Scanner;

public class hackerTranslate {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        //Creamos el diccionario
        HashMap<Character, String> hackerDict = new HashMap<>();
        hackerDict.put('A', "4");
        hackerDict.put('B', "l3");
        hackerDict.put('C', "[");
        hackerDict.put('D', ")");
        hackerDict.put('E', "3");
        hackerDict.put('F', "|=");
        hackerDict.put('G', "&");
        hackerDict.put('H', "#");
        hackerDict.put('I', "1");
        hackerDict.put('J', ",_|");
        hackerDict.put('K', ">|");
        hackerDict.put('L', "1");
        hackerDict.put('M', "/V|");
        hackerDict.put('N', "^/");
        hackerDict.put('O', "0");
        hackerDict.put('P', "|*");
        hackerDict.put('Q', "(_,)");
        hackerDict.put('R', "12");
        hackerDict.put('S', "5");
        hackerDict.put('T', "7");
        hackerDict.put('U', "(_)");
        hackerDict.put('V', "\\/");
        hackerDict.put('W', "\\/\\/");
        hackerDict.put('X', "><");
        hackerDict.put('Y', "j");
        hackerDict.put('Z', "2");

        //Pedimos que se inserte el texto
        System.out.print("Texto a traducir: ");
        String text = input.nextLine().toUpperCase();

        //Traduce el texto
        StringBuilder HackerText = new StringBuilder();
        for (int i = 0; i < text.length(); i++){
            char c = text.charAt(i);
            if (hackerDict.containsKey(c)){
                HackerText.append(hackerDict.get(c));
            }else{
                HackerText.append(c);
            }
        }
        System.out.println("Texto en Hacker: " + HackerText.toString());
    }
}
