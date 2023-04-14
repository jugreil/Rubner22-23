package Patterns.Proxy; 

public class SWDrucker implements Drucker {
    @Override
    public void drucken() {
        System.out.println("This is a black white text!");
    }
}