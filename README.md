### ZM0006-PID_Machine-Vision

# Image Preprocessing

In \Image_preprocessing\ is er een pipeline gemaakt voor het preprocessen van alle test images, hieraan kan worden toegevoegd.
Ook zorgt Image_preprocessing\PreProcessing.py er voor dat alle nieuwe .pdf bestanden in de folder test\P&ID_input worden omgezet naar het door het algoritme leesbare .png bestanen.


# Machine Vision

Binnen het mv.ipynb wordt het machine vision algoritme uitgevoerd, de folders die hiervoor worden gebruikt zijn gedefinieërd in het data.yaml.
Binnen het data.yaml staan ook alle objecten die herkend worden door het algoritme.

# Indeling

in \datasets\Labels_PID zijn de labels en plaatjes voor de training, validatie en test (gedeeltelijk) set te vinden. Hier kan aan worden toegevoegd door plaatjes met bounding boxes op makesense.ai of roboflow.com te maken en toe te voegen.

# Gebruik

Het mv.ipynb file dient gerunt te worden, hiervoor dient de gebruiker een stuk code te uncommenten voor het gebruiken van of de CPU of de GPU als rekenkracht voor het trainen en uitvoeren van het model.
