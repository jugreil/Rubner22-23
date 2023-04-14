package Patterns.Observer.Pull;

public class Farbsignal implements Anzeige {
    @Override
    public void getData(Messdaten messdaten) {
        System.out.printf("Messdaten werden dargestellt: Temperatur = %2f.%n", messdaten.getTemperatur());
    }
}
