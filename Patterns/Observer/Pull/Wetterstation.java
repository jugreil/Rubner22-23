package Patterns.Observer.Pull;

public class Wetterstation extends Zentrale {
    private Messdaten messdaten; 

    public void setData(Messdaten messdaten) {
        this.messdaten = messdaten; 
        sendData(messdaten);
    }

    public Messdaten getMessdaten() {
        return messdaten;
    }
}
