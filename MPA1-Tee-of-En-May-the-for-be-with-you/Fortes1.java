package teeofen;

import java.io.IOException;
import java.util.Scanner;
import java.nio.file.Path;
import java.nio.file.Paths;

// Instead of StringTokenizer, I decided to use Scanner 
//Source: Parse Text, http://www.javapractices.com/topic/TopicAction.do?Id=87

/**
 *
 * @author rdfortes
 */

// note: I accidentally interchange the terms for upperBound and lowerBound
// the initialization (i = 1) is the upperBound
// the condition ( i <= n) is the lowerBound

public class Fortes1 {
    
    int nProcess;
    int extraCount;
    String upperBound;
    String lowerBound;
    

    public static void main(String[] args) throws IOException {
        
        
        Fortes1 parser = new Fortes1("sample-test-cases.txt");
        parser.processLinebyLine();
        System.out.println();
        System.out.println("----- END OF TEXT -------");
    }
    
    public Fortes1(String fileName){
        filePath = Paths.get(fileName);
        nProcess = 0;
        extraCount = 0;
        upperBound = "";
        lowerBound = "";
    }
    
    // gets the currentLine in the file
    public final void processLinebyLine() throws IOException {
        try(Scanner sc = new Scanner(filePath)){
            while(sc.hasNextLine()){
                String currentLine = sc.nextLine();
                currentLine = currentLine.replaceAll("\\\\n", "");
                if((currentLine.contains("for"))) {
                    processLine(currentLine);
                } else if ((currentLine.contains("}"))) {
                    teeOfEn();
                } else {
                    processLine2(currentLine);
                }
            }
        }
    }
    
    // process the line with for(intitialization; condition; iteration)
    protected void processLine(String currentLine) {
        String tokens;
        nProcess = 0;
        extraCount = 0;
        upperBound = "";
        String temp = "";
        lowerBound = "";
        
        try (Scanner scan = new Scanner(currentLine)) {
            char[] stringTokens;
            int ctr = 0;
            String operators2 = "+*/-";
            scan.useDelimiter("\\s*for\\s*|\\n|[;(){}]+");
            while(scan.hasNext()){
                tokens = scan.next();
                // gets the upper bound value
                //System.out.println(tokens.trim());
                stringTokens = tokens.toCharArray();
                
                
                if(tokens.contains(" = ")) {
                    upperBound = tokens.substring(tokens.indexOf("=") + 2, tokens.length());
                    extraCount++;
                } 
                
                else if(tokens.contains("<=")) {
                    lowerBound = tokens.substring(tokens.indexOf("<=") + 3, tokens.length());
                    nProcess++;
                    extraCount++;
                    for(int i = 0; i < stringTokens.length; i++) {
                        if(operators2.indexOf(stringTokens[i]) >= 0){
                            ctr++;
                        }
                    }
                    
                } else if (tokens.contains(">")) {
                    lowerBound = tokens.substring(tokens.indexOf(">") + 2, tokens.length());
                    nProcess++;
                    extraCount++;
                    for(int i = 0; i < stringTokens.length; i++) {
                        if(operators2.indexOf(stringTokens[i]) >= 0){
                            ctr++;
                        }
                    }
                    
                } else if (tokens.contains("<")) {
                    lowerBound = tokens.substring(tokens.indexOf("<") + 2, tokens.length());
                    nProcess++;
                    extraCount++;
                    for(int i = 0; i < stringTokens.length; i++) {
                        if(operators2.indexOf(stringTokens[i]) >= 0){
                            ctr++;
                        }
                    }
                    
                } else if (tokens.contains(">=")) {
                    lowerBound = tokens.substring(tokens.indexOf("<=") + 3, tokens.length());
                    nProcess++;
                    extraCount++;
                    for(int i = 0; i < stringTokens.length; i++) {
                        if(operators2.indexOf(stringTokens[i]) >= 0){
                            ctr++;
                        }
                    }
                    
                }
                
                if ((tokens.contains("++"))) {
                    nProcess++;
                    break;
                } else if ((tokens.contains("--"))) {
                    nProcess++;
                    if(!"n".equals(upperBound)) {
                        temp = upperBound;
                        upperBound = lowerBound;
                        lowerBound = temp;
                    }
                    break;
                } else if ((tokens.contains("*="))) {
                    nProcess++;
                    lowerBound = "log(" + tokens.substring(tokens.indexOf("*=") + 3, tokens.length()) + ")" + lowerBound;
                    break;
                } else if ((tokens.contains("/="))) {
                    nProcess++;
                    if(!"n".equals(upperBound)) {
                        temp = upperBound;
                        upperBound = lowerBound;
                        lowerBound = temp;
                    }
                    break;
                } else if ((tokens.contains("+="))) {
                    nProcess++;
                    lowerBound = lowerBound + "/" + tokens.substring(tokens.indexOf("+=") + 3, tokens.length());
                    break;
                } else if ((tokens.contains("-="))) {
                    nProcess++;
                    if(!"n".equals(upperBound)) {
                        temp = upperBound;
                        upperBound = lowerBound;
                        lowerBound = temp;
                    }
                    break;
                }
            }
            if(ctr == 1) {
                lowerBound = "sqrt(" + lowerBound + ")";
            } else if (ctr == 2) {
                lowerBound = "cubert(" + lowerBound + ")";
            }
            nProcess = nProcess + ctr;
            extraCount = extraCount + ctr;
            //System.out.println("UpperBound: " + upperBound);
            //System.out.println("LowerBound: " + lowerBound);
        }
    }
    
    // gets the final number of processes after the curly braces
    protected void processLine2(String currentLine) {
        String tokens;
        String operators = "+=*/-";
        String operators2 = "+*/-";
        char[] stringTokens;
        
        try (Scanner scan = new Scanner(currentLine)) {
            //System.out.println(currentLine);
            scan.useDelimiter("\\s*for\\s*|\\n|[;(){}]+");
            while(scan.hasNext()){
                tokens = scan.next();
                // gets the upper bound value
                //System.out.println(tokens.trim());
                
                stringTokens = tokens.toCharArray();
                
                if((tokens.contains("++")) || (tokens.contains("--"))) {
                    nProcess++;
                    
                } else if ((tokens.contains("+=")) || (tokens.contains("-=")) || (tokens.contains("*="))) {
                    if((tokens.contains("+")) || (tokens.contains("-")) || (tokens.contains("*")) || (tokens.contains("/"))) {
                        for(int i = 0; i < stringTokens.length; i++) {
                            if(operators2.indexOf(stringTokens[i]) >= 0){
                                nProcess++;
                            }
                        }
                    }   
                } else {
                    for(int i = 0; i < stringTokens.length; i++) {
                        if(operators.indexOf(stringTokens[i]) >= 0){
                            nProcess++;
                        }
                    }
                }
            }
        }
    }
    
    
    protected void teeOfEn() {
        /* if upperB = 1, nProcess * lowerB + extraCount
                    else, lowerB (n - upperB + 1) + extraCount
        */
       
       String teeOfEn;
       String nProcesses;
       String extraCounts;
       
       nProcesses = String.valueOf(nProcess);
       extraCounts = String.valueOf(extraCount);
       
       
       if (("n".equals(upperBound) && ("1".equals(lowerBound)))) {
           teeOfEn = extraCounts;
       } else if ("1".equals(upperBound)) {
           teeOfEn = nProcesses + " * " + lowerBound + " + " + extraCounts;
       } else {
           teeOfEn = nProcesses + " (" + lowerBound + " - " + upperBound + " + 1) + " + extraCounts;
       }
       System.out.println("T(n) = " + teeOfEn);
    }
    
    final Path filePath;
        
}
