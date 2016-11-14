package edu.csula.cs454.es;

import java.io.File;

/**
 * Main Cli application for the elastic search programming quiz app
 */
public class Application {
    public static void main(String[] args) {
        // TODO parse command argument and do parsing and searching accordingly
        System.out.println("Start your home depot product search today");
        
        HomeDepotSearch search = new HomeDepotSearch();
        
        String pd = "C:/Users/Jaymin/Desktop/cs454-winter-2016-master/src/test/resources/product_descriptions.csv";
    	String att = "C:/Users/Jaymin/Desktop/cs454-winter-2016-master/src/test/resources/attributes.csv";

    	File PD = new File(pd);
    	File ATT = new File(att);
        search.parseData(PD, ATT);
    }
}
