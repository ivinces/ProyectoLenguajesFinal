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

public class Archivo {
    
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
    
    public static ArrayList<Universidades> separartag(ArrayList<String> lista,String tag) throws UnsupportedEncodingException{
        ArrayList<Universidades> lista2=new ArrayList<>();
        for(Object linea:lista){
            String cadena=String.valueOf(linea);
            //System.out.println(cadena);
            if(cadena.length()!=0){
                String[] cad=cadena.split(",");
                
                int posicion=Integer.parseInt(cad[0]);
                String unis=URLDecoder.decode(cad[1], "UTF-8");
                System.out.println(unis);
                Universidades uni_posi=new Universidades(unis,posicion);
                lista2.add(uni_posi);
                }
            }
        return lista2;
    
    }

}
