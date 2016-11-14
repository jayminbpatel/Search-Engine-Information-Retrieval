package homework3;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Indexing {
	
	public static void main(String[]args)
    {
        File curDir = new File("C:/Users/Jaymin/Downloads/en/articles/");
        getAllFilse(curDir);
    }
    private static void getAllFilse(File curDir) {

        File[] filesList = curDir.listFiles();
        for(File f : filesList){
            if(f.isDirectory())
            {
            	getAllFilse(f);
        		System.out.println(f.getName());
            }
            
            if(f.isFile())
            {	
            	StringBuilder contentBuilder = new StringBuilder();
            	try {
            	    BufferedReader in = new BufferedReader(new FileReader(f));
            	    String str;
            	    while ((str = in.readLine()) != null) {
            	        contentBuilder.append(str);
            	    }
            	    in.close();
            	} catch (IOException e) {
            	}
            	String content = contentBuilder.toString();
            	System.out.println(content);
            	content = "";
            
            	System.out.println(f.getName());
            }
        }

    }

}
