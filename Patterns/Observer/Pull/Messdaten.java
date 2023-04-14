package Patterns.Observer.Pull;

public class Messdaten {
    private float temperatur; 
    private float luftfeuchtigkeit; 

    public Messdaten(float temperatur, float luftfeuchtigkeit) {
        this.temperatur = temperatur; 
        this.luftfeuchtigkeit = luftfeuchtigkeit; 
    }

    public float getLuftfeuchtigkeit() {
        return luftfeuchtigkeit;
    }
    
    public float getTemperatur() {
        return temperatur;
    }
}
