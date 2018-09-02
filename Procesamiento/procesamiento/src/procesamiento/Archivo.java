/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package procesamiento;



import java.util.ArrayList;
import java.io.*;
import org.json.JSONArray;
import org.json.JSONObject;
import org.json.JSONException;
import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
import java.util.Collection;
import java.util.Collections;
import java.util.Hashtable;

public class Archivo {
    static Hashtable<String,Posiciones> ht=new Hashtable<>();
    // Método mostrar Contenido
    public static ArrayList muestraContenido(String archivo) throws FileNotFoundException, IOException {
        ArrayList lectura = new ArrayList();
        String cadena;
        FileReader f = new FileReader(archivo);     
        try (BufferedReader b = new BufferedReader(f)) {        // Uso de FileReader y Bufferred para leer archivo
            while((cadena = b.readLine())!=null) {
                lectura.add(cadena);
                //System.out.println(cadena);
            }
        }
        return lectura;
    }
    
    // Método eliminar archivo
    public static void eliminaArchivo(String nombreArchivo) {
        File fichero = new File(nombreArchivo);
        fichero.delete();
    }
    
    // Método modificar contenido
    public static void modificarContenido(ArrayList<Universidades> nombreArrayList, String nombreArchivo)throws FileNotFoundException, IOException, JSONException {
        eliminaArchivo(nombreArchivo);  // Uso de método eliminar archivo
        String cadena;
        File directorio = new File("Procesado");
        directorio.mkdir();
        try (FileWriter fichero = new FileWriter("Procesado/"+nombreArchivo)) {
            JSONArray list=new JSONArray();
            JSONObject f = new JSONObject();
            for (Universidades linea : nombreArrayList) {
                JSONObject obj = new JSONObject();
		obj.put("posicion", linea.getPosicion());
		obj.put("universidad", linea.getUniversidad());
		
                list.put(obj);
            }
            f.put("entradas", list);
            try{

                    fichero.write(f.toString());



            }catch(Exception ex){
                    System.out.println("Error: "+ex.toString());
            }
            fichero.flush();
            fichero.close();
        }
        
    }
    
    public static void modificarContenido2(String nombreArchivo)throws FileNotFoundException, IOException, JSONException {
        eliminaArchivo(nombreArchivo);  // Uso de método eliminar archivo
        String cadena;
        File directorio = new File("Procesado");
        directorio.mkdir();
        try (FileWriter fichero = new FileWriter("Procesado/"+nombreArchivo)) {
            JSONArray list=new JSONArray();
            JSONObject f = new JSONObject();
            
            for (String linea : Collections.list(ht.keys())) {
                JSONObject obj = new JSONObject();
		obj.put("universidad", linea);
                Posiciones p=ht.get(linea);
                obj.put("p_mundial", p.getMundial());
                obj.put("p_pais", p.getPais());
                obj.put("p_2006", p.getAnio2006());
                obj.put("p_2007", p.getAnio2007());
                obj.put("p_2008", p.getAnio2008());
                obj.put("p_2009", p.getAnio2009());
                obj.put("p_2010", p.getAnio2010());
		obj.put("p_2011", p.getAnio2011());
                obj.put("p_2012", p.getAnio2012());
                obj.put("p_2013", p.getAnio2013());
                obj.put("p_2014", p.getAnio2014());
                obj.put("p_2015", p.getAnio2015());
                obj.put("p_fisica", p.getArea_fisica());
                obj.put("p_quimica", p.getArea_quimica());
                obj.put("p_computacion", p.getArea_computacion());
                obj.put("p_ing", p.getArea_ingenieria());
                obj.put("p_mate", p.getArea_matematica());
                obj.put("p_science", p.getArea_science());
                obj.put("p_sociales", p.getArea_sociales());
                obj.put("p_economia", p.getArea_economia());
                obj.put("p_medicina", p.getArea_medicina());
                
                list.put(obj);
            }
            f.put("entradas", list);
            try{

                    fichero.write(f.toString());



            }catch(Exception ex){
                    System.out.println("Error: "+ex.toString());
            }
            fichero.flush();
            fichero.close();
        }
        
    }
    
    public static ArrayList<Universidades> separartag(ArrayList<String> lista,String tag, String ruta) throws UnsupportedEncodingException{
        ArrayList<Universidades> lista2=new ArrayList<>();
        for(Object linea:lista){
            String cadena=String.valueOf(linea);
            //System.out.println(cadena);
            if(cadena.length()!=0){
                String[] cad=cadena.split(",");
                int posicion=Integer.parseInt(cad[0]);
                String unis=cad[1].split("/")[0].replace("\\n", "");
                System.out.println(unis);
                Universidades uni_posi=new Universidades(unis,posicion);
                lista2.add(uni_posi);
                
                if(ruta.equals("Anios")){
                    if(tag.equals("2006")){
                        if(ht.containsKey(unis)){
                            ht.get(unis).setAnio2006(posicion);
                        }
                        else{
                            Posiciones p=new Posiciones();
                            p.setAnio2006(posicion);
                            ht.put(unis, p);
                        }
                    }
                    if(tag.equals("2007")){
                        if(ht.containsKey(unis)){
                            ht.get(unis).setAnio2007(posicion);
                        }
                        else{
                            Posiciones p=new Posiciones();
                            p.setAnio2007(posicion);
                            ht.put(unis, p);
                        }
                    }
                    if(tag.equals("2008")){
                        if(ht.containsKey(unis)){
                            ht.get(unis).setAnio2008(posicion);
                        }
                        else{
                            Posiciones p=new Posiciones();
                            p.setAnio2008(posicion);
                            ht.put(unis, p);
                        }
                    }
                    if(tag.equals("2009")){
                        if(ht.containsKey(unis)){
                            ht.get(unis).setAnio2009(posicion);
                        }
                        else{
                            Posiciones p=new Posiciones();
                            p.setAnio2009(posicion);
                            ht.put(unis, p);
                        }
                    }
                    if(tag.equals("2010")){
                        if(ht.containsKey(unis)){
                            ht.get(unis).setAnio2010(posicion);
                        }
                        else{
                            Posiciones p=new Posiciones();
                            p.setAnio2010(posicion);
                            ht.put(unis, p);
                        }
                    }
                    if(tag.equals("2011")){
                        if(ht.containsKey(unis)){
                            ht.get(unis).setAnio2011(posicion);
                        }
                        else{
                            Posiciones p=new Posiciones();
                            p.setAnio2011(posicion);
                            ht.put(unis, p);
                        }
                    }
                    if(tag.equals("2012")){
                        if(ht.containsKey(unis)){
                            ht.get(unis).setAnio2012(posicion);
                        }
                        else{
                            Posiciones p=new Posiciones();
                            p.setAnio2012(posicion);
                            ht.put(unis, p);
                        }
                    }
                    if(tag.equals("2013")){
                        if(ht.containsKey(unis)){
                            ht.get(unis).setAnio2013(posicion);
                        }
                        else{
                            Posiciones p=new Posiciones();
                            p.setAnio2013(posicion);
                            ht.put(unis, p);
                        }
                    }
                    if(tag.equals("2014")){
                        if(ht.containsKey(unis)){
                            ht.get(unis).setAnio2014(posicion);
                        }
                        else{
                            Posiciones p=new Posiciones();
                            p.setAnio2014(posicion);
                            ht.put(unis, p);
                        }
                    }
                    if(tag.equals("2015")){
                        if(ht.containsKey(unis)){
                            ht.get(unis).setAnio2015(posicion);
                        }
                        else{
                            Posiciones p=new Posiciones();
                            p.setAnio2015(posicion);
                            ht.put(unis, p);
                        }
                    }
                }
                if(ruta.equals("Paises")){
                    if(ht.containsKey(unis)){
                            ht.get(unis).setPais(posicion);
                        }
                        else{
                            Posiciones p=new Posiciones();
                            p.setPais(posicion);
                            ht.put(unis, p);
                        }

                }
                if(ruta.equals("Mundial")){
                    if(ht.containsKey(unis)){
                            ht.get(unis).setMundial(posicion);
                        }
                        else{
                            Posiciones p=new Posiciones();
                            p.setMundial(posicion);
                            ht.put(unis, p);
                        }

                }
                if(ruta.equals("Area")){
                    if(tag.equals("Computacion")){
                        if(ht.containsKey(unis)){
                            ht.get(unis).setArea_computacion(posicion);
                        }
                        else{
                            Posiciones p=new Posiciones();
                            p.setArea_computacion(posicion);
                            ht.put(unis, p);
                        }
                    }
                    if(tag.equals("Economia")){
                        if(ht.containsKey(unis)){
                            ht.get(unis).setArea_economia(posicion);
                        }
                        else{
                            Posiciones p=new Posiciones();
                            p.setArea_economia(posicion);
                            ht.put(unis, p);
                        }
                    }
                    if(tag.equals("Fisica")){
                        if(ht.containsKey(unis)){
                            ht.get(unis).setArea_fisica(posicion);
                        }
                        else{
                            Posiciones p=new Posiciones();
                            p.setArea_fisica(posicion);
                            ht.put(unis, p);
                        }
                    }
                    if(tag.equals("Ingenieria")){
                        if(ht.containsKey(unis)){
                            ht.get(unis).setArea_ingenieria(posicion);
                        }
                        else{
                            Posiciones p=new Posiciones();
                            p.setArea_ingenieria(posicion);
                            ht.put(unis, p);
                        }
                    }
                    if(tag.equals("Matematicas")){
                        if(ht.containsKey(unis)){
                            ht.get(unis).setArea_matematica(posicion);
                        }
                        else{
                            Posiciones p=new Posiciones();
                            p.setArea_matematica(posicion);
                            ht.put(unis, p);
                        }
                    }
                    if(tag.equals("Medicina")){
                        if(ht.containsKey(unis)){
                            ht.get(unis).setArea_medicina(posicion);
                        }
                        else{
                            Posiciones p=new Posiciones();
                            p.setArea_medicina(posicion);
                            ht.put(unis, p);
                        }
                    }
                    if(tag.equals("Quimica")){
                        if(ht.containsKey(unis)){
                            ht.get(unis).setArea_quimica(posicion);
                        }
                        else{
                            Posiciones p=new Posiciones();
                            p.setArea_quimica(posicion);
                            ht.put(unis, p);
                        }
                    }
                    if(tag.equals("Science")){
                        if(ht.containsKey(unis)){
                            ht.get(unis).setArea_science(posicion);
                        }
                        else{
                            Posiciones p=new Posiciones();
                            p.setArea_science(posicion);
                            ht.put(unis, p);
                        }
                    }
                    if(tag.equals("Sociales")){
                        if(ht.containsKey(unis)){
                            ht.get(unis).setArea_sociales(posicion);
                        }
                        else{
                            Posiciones p=new Posiciones();
                            p.setArea_sociales(posicion);
                            ht.put(unis, p);
                        }
                    }
                }
                
            }
            
        }
        return lista2;
    
    }

}
