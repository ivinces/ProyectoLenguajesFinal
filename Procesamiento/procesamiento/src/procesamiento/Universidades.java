/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package procesamiento;

/**
 *
 * @author isabe
 */
public class Universidades {
    private String Universidad;
    private int posicion;

    public Universidades(String Universidad, int posicion) {
        this.Universidad = Universidad;
        this.posicion = posicion;
    }

    public String getUniversidad() {
        return Universidad;
    }

    public void setUniversidad(String Universidad) {
        this.Universidad = Universidad;
    }

    public int getPosicion() {
        return posicion;
    }

    public void setPosicion(int posicion) {
        this.posicion = posicion;
    }
    
    
}
