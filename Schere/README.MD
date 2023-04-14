In der Game.py läuft das Spiel ab. Dabei wird mit Mediapipe die Positionsdaten der Hand herbeigeholt. Diese Daten werden dann mit den hinterlegten positionsdaten verglichen. Das mit am wenigsten abweichung wird verwendet.
In der Server.py sind die einfachen Server funktionen.
In der Test.py wird für jede Figur die basisdaten aufgenommen und abgespeichert. Somit hat man 1000 Einträge zu jeder Figur.
Falls man eine weitere Figur hinzufügen will muss man nur dieses Proramm ausführen.
Desweiteren muss mann dann noch das getAverage.py Programm ausführen. Dieses nimmt den durchschnitt über  diese 1000 Einträge. 

Ich habe auch noch ein Programm geschrieben testForDoubleAi, diese nimmt nun diese 20 Punkte als eingang und versucht Schere Stein oder Papier zu prediction.
Dies funktioniert aber nicht so gut wie das mit dem Vergleichen deshalb nicht implementiert.