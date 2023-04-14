package Patterns.Observer.Pull;

public class Client {
    public static void main(String[] args) {
        Wetterstation wetterstation = new Wetterstation(); 
        wetterstation.addAnzeige(new Bildschirm());
        Farbsignal farbsignal = new Farbsignal(); 
        wetterstation.addAnzeige(farbsignal);

        wetterstation.setData(new Messdaten(20.8f, 60.5f));
        wetterstation.removeAnzeige(farbsignal);
        wetterstation.setData(new Messdaten(22.8f, 55.5f));
        
    }
}
