/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package procesamiento;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import org.json.JSONException;

/**
 *
 * @author Fanny
 */
public class Procesamiento {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException, FileNotFoundException, JSONException {
        
        String anios[]={"2006.csv","2007.csv","2008.csv","2009.csv","2010.csv"
        ,"2011.csv","2012.csv","2013.csv","2014.csv","2015.csv"};
        String area[]={"Computacion.csv","Economia.csv","Fisica.csv","Ingenieria.csv","Matematicas.csv"
        ,"Medicina.csv","Quimica.csv","Science.csv","Sociales.csv"};
        String mundialShangai[]={"Mundo.csv"};
        String mundialWebometrics[]={"World.csv"};
        String paises[]={"África.csv","Alemania.csv","América del Norte.csv","Americas.csv"
        ,"Arab_world.csv","Argentina.csv","Asia (incl ME).csv","Asia-Pacifico.csv","Australia.csv"
        ,"Brasil.csv","Canadá.csv","Caribe.csv","Chile.csv","China.csv","Corea del Sur.csv"
        ,"Ecuador.csv","EEUU.csv","Egipto.csv","Emiratos Árabes Unidos.csv","Estados Unidos de América.csv"
        ,"Europa.csv","Francia.csv","Italia.csv","Japón.csv","Latinoamérica.csv","Medio Oriente.csv"
        ,"México.csv","Nueva Zelanda.csv","Oceania.csv","Rusia.csv","Sudasia.csv"
        ,"Sudeste Asiático.csv","Tailandia.csv"};
        
        recorrido(anios,"Shangai/Anios");
        recorrido(area,"Shangai/Area");
        recorrido(mundialShangai,"Shangai/Mundial");
        recorrido(mundialWebometrics,"Webometrics/Mundial");
        recorrido(paises,"Webometrics/Paises");
        
        // TODO code application logic here
    }
    
    public static void recorrido(String[] arreglo, String ruta) throws IOException, FileNotFoundException, JSONException{
        for(String archivo: arreglo){
            String rutanueva="Scraping/"+ruta+"/"+archivo;
            ArrayList lec=Archivo.muestraContenido(rutanueva);
            String nombre=archivo.split(".csv")[0];
            System.out.println(">>>>>>>>>>>>>>>>>>"+nombre+"<<<<<<<<<<<<<<<");
            
            ArrayList<Universidades> tags=Archivo.separartag(lec, nombre);
            Procesar p=new Procesar();
            p.procesarporposicion(tags,nombre);
        }
    }
    
    
    
}