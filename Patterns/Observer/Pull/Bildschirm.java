package Patterns.Observer.Pull;

public class Bildschirm implements Anzeige {

    @Override
    public void getData(Messdaten messdaten) {
        System.out.printf("Messdaten erhalten: Temperatur = %2f & Luftfeuchtigkeit = %2f.%n", messdaten.getTemperatur(), messdaten.getLuftfeuchtigkeit());
    }
    
}
