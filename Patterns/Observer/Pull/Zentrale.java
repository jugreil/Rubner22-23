package Patterns.Observer.Pull;

import java.util.ArrayList;
import java.util.List;

public abstract class Zentrale {
    
    private List<Anzeige> anzeigeList = new ArrayList<Anzeige>(); 

    public void addAnzeige(Anzeige anzeige) {
        anzeigeList.add(anzeige); 
    }

    public void removeAnzeige(Anzeige anzeige) {
        anzeigeList.remove(anzeige); 
    }

    protected void sendData(Messdaten messdaten) {
        for(Anzeige anzeige : anzeigeList) {
            anzeige.getData(messdaten); 
        }
    }
}
