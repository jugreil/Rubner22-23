package Patterns.Proxy; 

public class ColorDrucker implements Drucker{

    @Override
    public void drucken() {
        System.out.println("This is a colored text!");
    }
    
}