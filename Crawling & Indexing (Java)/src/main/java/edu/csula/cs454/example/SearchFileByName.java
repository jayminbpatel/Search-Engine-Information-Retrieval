package edu.csula.cs454.example;

import java.io.File;
import java.util.LinkedList;

public class SearchFileByName {

	public static void main(String args[]) {
		
		find("milin.txt", "C:/Users/Jaymin/Desktop");
	}	
		public static void find(String source,String rep) {
		    String pattern = source;
		    LinkedList<File> qu = new LinkedList<File>();
		    File src = new File(rep);
		    qu.add(src);
		    while(!qu.isEmpty()) {
		        File srcc = qu.removeFirst();
	
		        if(srcc!=null && srcc.exists()) {
		            if (srcc.isDirectory()) {
		                File[] tab=srcc.listFiles();
		                for(File s: srcc.listFiles()) {
		                    qu.addLast(s);
		                }
		            } else if (srcc.isFile()) {
		                if(srcc.getName().equals(pattern)) {
		                    System.out.println(srcc.getName());
		                }
		            }
		        }
		    }
		}
	
}
