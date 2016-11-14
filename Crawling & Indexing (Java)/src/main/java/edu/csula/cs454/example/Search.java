package edu.csula.cs454.example;

import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;

public class Search {
	 public static void main(String[] args) {
		 
		    File folder = new File("C:/Users/Jaymin/Downloads/en/articles");

		    ArrayList<File> files = new ArrayList<File>(Arrays.asList(folder.listFiles()));
		    ArrayList<String> temp = new ArrayList<String>();
		    File subFolder;

		    for(File f : files) {
		    	if (f.isFile()) {
		    		System.out.println("File: " + f.getName());
		    	} else if (f.isDirectory()) {
		    		temp.add(f.toString());
		    		System.out.println("Directory: " + f.getName());
		    	}
		    }
		    
		    System.out.println("------------------------------------------------------------");

		    //ArrayList<File> subFiles;
		    File[] subFiles;
		    for(int i = 0; i < temp.size(); i++) {
		    	subFolder = new File(temp.get(i));
		    	//subFiles = new ArrayList<File> (Arrays.asList(subFolder.listFiles()));
		    	subFiles = subFolder.listFiles();
		    	try {
		    		for(File f : subFiles) {
		    			if (f.isFile()) {
		    				System.out.println(temp.get(i) + " , " + "File: " + f.getName());
		    			} else if (f.isDirectory()) {
		    				System.out.println(temp.get(i) + " , " + "Directory: " + f.getName());
		    			}
		    		} 
		    	}	catch (Exception e) {
		    		System.out.println("Access Denied for file:- \"" + temp.get(i) + "\"");
		    	}
		    		
			    System.out.println("------------------------------------------------------------");
		    }
		   
	 }	 
}
