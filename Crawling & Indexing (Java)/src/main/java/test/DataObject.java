package test;

import java.util.ArrayList;
import java.util.List;

public class DataObject {

	private String url = "https://www.wikipedia.org/";
	private int level = 1;
	private int count = 1;
/*	private List<String> list = new ArrayList<String>() {
	  {
		add("String 1");
		add("String 2");
		add("String 3");
	  }
	};
*/
	//getter and setter methods

	@Override
	public String toString() {
	  // return "DataObject [url = " + url + ", level = " + level + ", count = " + count + "]";
	   
	   return "{" +
		  			"\"url\" : \" " + url + "\", " +
		  			" \"level\" : " + level + "," +
		  			" \"count\" : " + count +
		  		"}";
	}

}