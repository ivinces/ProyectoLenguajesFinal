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
 * @author isabe
 */
public class Procesar {

    public Procesar() {
    }
    
    public void procesarporposicion(ArrayList<Universidades> uni,String nombre) throws IOException, FileNotFoundException, JSONException{
        uni.sort((Universidades e1, Universidades e2)->e2.getPosicion()-e1.getPosicion());
        Archivo.modificarContenido(uni,nombre+".json");
        
    }
}
