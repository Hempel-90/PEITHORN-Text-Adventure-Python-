#Textadventure Peithorn

#region Import, Funktion und While -Schleife

import time

def TextOutputIntervall(Text): #<== Funktion für die einzelne Ausgabe der Buchstaben.
    for i in Text:
        print(i,end= "")
        time.sleep(0.05)

while True: #<== While-Schleife um das Spiel immer wieder neuzustarten.

#endregion
   
#region Intro

    Intro = "Willkommen in der Welt von...\n\n"
    Intro2 = ["||||||------------||||||------------||||   PEITHORN   ||||------------||||||------------||||||\n\n"]
    
    Intro3 = Intro.center(120) 
    Intro4 = Intro2[0].center(115)
    print(Intro3)
    print(Intro4)

    # time.sleep(1)
    
    Steuerung = "Steuerung:\n\nTasten 1, 2, 3 und dann Enter.\nEs gelten nur die aufgeführten Zahlen und auch nur wenn diese auch zur Auwahl stehen!\nDie einzige Ausnahme ist die Namenseingabe.\nAlle anderen Eingaben führen zu einem Game Over, also merken Sie es sich gut!"
    
    TextOutputIntervall(Steuerung)

    #endregion

#region Vorstellung

    Vorstellung1 = "\n\nAlso fangen wir an...Erstmal zu mir, ich bin der Erzähler und werde Sie bei Ihrer kompletten Reise hier begleiten.\n\nNun zu Ihnen...\n"
    TextOutputIntervall(Vorstellung1)

    # time.sleep(1)

    Namefrage = "\nZuerst einmal, wie ist Ihr Name?\n"
    TextOutputIntervall(Namefrage)
    Name = input("\n")

    Willkommen = (f"\nHerzlichen Willkommen {Name}...")
    TextOutputIntervall(Willkommen)
    
    #region Klassenwahl

    Klassenauswahl = "\nNun wählen Sie Ihre Klasse, mein Freund...\n"
    TextOutputIntervall(Klassenauswahl)

    Klassen = [{"Klassen": "\n1. Krieger \n2. Ritter\n3. Dieb\n"}]
    TextOutputIntervall(Klassen[0]["Klassen"])
    
    Klassenwahl = input("\n")
    if Klassenwahl == "1":
        Wahl1 ="\nAh verstehe, Sie sind also ein Krieger, stehen wohl auf Männer im Pelzschlüpfer.\n"           
        TextOutputIntervall(Wahl1)
    elif Klassenwahl == "2":
        Wahl2 = "\nEin Ritter also, klischeemäßiger geht es wohl nicht, Sie Langweiler.\n"
        TextOutputIntervall(Wahl2)
    elif Klassenwahl == "3":
        Wahl3 = "\nSie sind also ein Dieb, also lass ich meinen Goldbeutel besser nicht in Ihrer Nähe.\n"
        TextOutputIntervall(Wahl3)
    else:
        Wahl4 = "\nIch weiß zwar nicht was das sein soll, aber wir machen trotzdem weiter...\n"
        TextOutputIntervall(Wahl4)

    #endregion
    
#endregion

#region Story

#region Listen

    #Auswahlliste = Fragen und Antworten für die jeweiligen Entscheidungen.
    
    Auswahlliste = [{"Frage": "\nWelchen Weg wollen Sie nehmen?\n", "Antworten": "1. Geh ins Gebirge""\n2. Geh zum Wald"},
                    {"Frage": "\nWelchen Weg wählen Sie?\n", "Antworten": "1. Gebirge""\n2. Tal"},
                    {"Frage": "\nWas wollen Sie tun?\n", "Antworten": "1. Angreifen""\n2. Reden"},
                    {"Frage": "\nWofür entscheiden Sie sich?\n", "Antworten": "1. Hexenhaus""\n2. Lichtung"},                   
                    {"Frage": "\nWas tun Sie?\n", "Antworten": "1. Erschlagen""\n2. Reden"},
                    {"Frage": "\nWelchen Weg schlagen Sie ein?\n", "Antworten": "1. Westen""\n2. Osten"},
                    {"Frage": "\nFür was entscheiden Sie sich?\n", "Antworten": "1. nach Hause""\n2. Brücke""\n3. Baumstämme"},
                    {"Frage": "\nWie entscheiden Sie sich?\n", "Antworten": "1. Reden""\n2. Erschlagen"}
                    ]
    
    #Antwortenlist = Antworten auf die Auswahl des Spielers aus der Auswahlliste und Haupttext für die Geschichte.
    
    Antwortenliste = [{"Antworten":["\nSie sind ins Gebirge gegangen.\n\nVor Ihnen liegt eine Schlucht mit steilen Felswänden zu beiden Seiten.\nSie sind in der Schlucht und vor Ihnen spaltet sich der Weg. Zum einen geht es zur linken Seite nach oben weiter\nins Gebirge, zum anderen geht es zu Ihrer rechten, in ein Tal.\n\n", 
                                    "\nSie sind zum Wald gegangen.\n\nSie sehen einen dunklen Pfad der weiter in den Wald führt. Sie sind auf dem dunklen Pfad.\nÜberall um Sie herum ist das Dickicht so dicht das Sie nichts sehen außer Bäume und Büsche,\nbis Sie zu einer Gabelung kommen. Dort steht ein Schild: Links Hexenhaus, Rechts Lichtung.\n\n"]},
                    {"Antworten":["\nSie sind weiter ins Gebirge gegangen und treffen auf einen fetten, hässlichen Bergtroll.\n\nAls dieser Sie bemerkt, müssen Sie sich entscheiden...\n\n", 
                                    "\nSie haben sich für das Tal entschieden...\n\nHier steht ein kleines Haus und davor eine kleine bärtige Gestalt...ein Zwerg.\nSie sprechen ihn an...\n\nSie: Hey Zwerg, du könntest mir nicht zufällig den Weg zur Schlangen-Höhle weisen?\n\nZwerg: Was heißt hier Zwerg, du krummnasiger Hodenkobold! Ich bin kein Zwerg,\nich habe nur bei einem Unfall im Gebirge beide Beine verloren und jetzt stecke ich meine Stümpfe\neinfach in meine Stiefel!\nNun gut ich helfe dir...\nDu musst einfach weiter nach Osten gehen bis du zum Sumpf kommst und diesen durchqueren...\nAber sei gewarnt der Sumpf ist tükisch...Lebewohl!\n\nErzähler: Wie der 'Zwerg' sagte, gehen Sie weiter nach Osten durch das Tal, der Weg ist leicht zu bewältigen.\nAls Sie das Tal verlassen, finden Sie sich in einem Sumpf wieder.\n\n"]},
                    {"Antworten":["\nSie haben sich dafür entschieden ihn anzugreifen...\n\nSchlechte Entscheidung, denn dieser wischt mit Ihnen den Boden und Sie sterben eines graumsamen Todes als\ndieser Ihnen alle Gliedmaßen ausreißt...\n\nGame Over!\n\n",
                                    "\nSie versuchen mit dem Troll zu reden...\n\nSie: Hey du hässliches Ungetüm, ich will keinen Ärger, ich wollte dich nur nach dem Weg zur Schlangen-Höhle fragen...\n\nTroll: Das geht auch freundlicher, du Sohn eines Fettdrachen...\nAber nun gut dadrüber werde ich mal hinwegsehen...\nDu kannst den Bergpass in Richtung Osten nehmen und solltest dann in der Nähe der Höhle sein.\n\nErzähler: Somit begeben Sie sich auf dem Berpfad Richtung Osten, der Weg ist anstregend und Ihnen begegnen manche\nGefahren, aber letztendlich schaffen Sie es über den Pass und finden sich in einem Sumpf wieder."]},
                        {"Antworten": ["\nSie sind zum Hexenhaus gegangen und kolpfen an die Tür...\n\nZuerst hören Sie eine fürchtlich grässliche Stimme, die sagt 'einen Moment bitte!',\neinige Zeit später stellen Sie fest das die Person dazu noch grässlicher ist...\n\nAls die alte, runzelige, krummnasige, warzige, bucklige...('ach lassen wir das')...Hexe Ihnen die Tür öffnet.\nSie schrecken vor dieser scheußlichen Gestalt zurück und überlegen was Sie tun wollen...\n\n",
                                    "\nSie sind zur Lichtung gegangen.\n\nDie Lichtung erweist sich als äußerst friedlich, aber auch ziemlich langweilig und somit gehen Sie weiter in den Wald...\nSie befinden sich nun in den 'Tiefen des Waldes' und es erschließen sich Ihnen zwei Wege...\nDer eine geht nach Westen, der andere nach Osten...\n\n"]},
                        {"Antworten":["\nSie haben sich dazu entschieden sie zu erschlagen.\n\nSie rammen ihr Ihr Schwert zwischen ihre heraussteheden Augen, reißen Ihr Schwert nach oben und\nentfernen ihr so ihre hässliche Rübe von ihrem scheußlichen Körper...\n\nAnschließend durchsuchen Sie das Haus der Hexe und finden einige menschliche Überreste,\ndie die Hexe wohl verspeist hat...bei einer Leiche finden Sie eine Karte der Gegend,\ndie Ihnen den Weg zu ihrem Ziel weist...\n\nAngewidert verlassen Sie das Haus und setzten es in Brand...danach setzen Sie ihren Weg fort,\nder Sie in einen Sumpf führt.\n\n",
                                    "\nSie haben sich entschieden mit ihr zu reden.\n\nDie Hexe bittet Sie herein und bietet Ihnen Tee an, den Sie dankend annehmen.\n\nHexe: Also wo möchten Sie denn hin mein junger Freund?\n\nSie: Zur Schlangen-Höhle, aber ich kenne den Weg nicht...\n\nHexe: Oh das ist eine gefährliche Gegend, aber das wirst du eh nicht mehr erfahren du Idiot!\n\nSie: Was zum...\n\nErzähler: Ihr Tee war vergiftet und Sie verlieren das Bewusstsein bis Sie letztendlich sterben und\ndie Hexe Sie zerstückelt, Ihre Überreste in den Ofen wirft und Sie verspeist...\n\nGame Over!\n\n"]},
                        {"Antworten": ["\nSie haben sich für den Weg nach Westen entschieden.\n\nNach einiger Zeit die Sie an einem Fluss der durch den Wald führt entlang gegangen sind,\nändert sich das Erscheinungsbild der Gegend, die Bäume werden etwas weniger, dafür das Wasser mehr...\n\nSie sind in einem Sumpf gelandet.\n\n",
                                    "\nSie haben sich für den Weg nach Osten entschieden.\n\nDer Wald wird immer dichter und wird zu einem richtigen Labyrinth...\nNach Tagen langem herum irrens werden Sie unvorsichtig und stürzen einen Abhang hinunter und brechen sich ein Bein...\nDa sich ihr Bein dermaßen verdreht hat, so das auch ihr Knochen aus eben diesem heraus ragt,\nsind Sie nicht mehr in der Lage weiter zu gehen und sterben eines elendigen Todes...\n\nGame Over!\n\n"]},
                        {"Antworten": ["\nDer Sumpf stellt sich als äußert schwierig zu durchqueren heraus.\nEs stellen sich Ihnen drei Entscheidungen...\nZum einen könnten Sie wieder umkehren und nach Hause gehen, zum anderen erschließen sich Ihnen zwei Wege...\nDer eine führt über eine alte Holz-Brücke direkt zur Schlangen-Höhle und\nder andere über mehrere Baumstämme über einen längeren Weg...\n\n"]},
                        {"Antworten": ["\nSie haben sich entschieden nach Hause zu gehen.\nNach einer langen und kräftezehrenden Reise, sind Sie endlich wieder Zuhause\nund leben ihr einfaches, aber friedvolles Leben weiter...\n\nEnde.\n\n",
                                    "\nSie haben sich für die Brücke entschieden.\nDie Brücke knarrzt unter ihrem Gewicht immer wieder verdächtig,\nSie haben ungefähr die Hälfte bis zur Höhle hinter sich gebracht, als Sie ein komisches gurgelndes Geräusch vernehmen...\nWie aus dem nichts schießt ein fürchterliches Ungetüm aus dem Sumpf...\nEs sieht aus wie eine Mischung aus einer Kröte(Körper), einem Alligator(Kopf) und einem Oktopus(Gliedmaßen).\nSie versuchen es zu erschlagen, aber ohne Erfolg, es packt sie mit seinem widerwertigen Armen,\nreißt sie mit diesen in zwei Hälften und verschlingt Sie mit einem Haps...\n\nGame Over!\n\n",
                                    "\nSie haben sich für die Baumstämme entschieden.\nDie Baumstämme sind äußert rutschig und Sie drohen des öfteren abzurutschen...\n\nDoch irgendwie schaffen Sie es sich den Weg durch den Sumpf bis zur Höhle zu erkämpfen und\nstehen nun vor ihrem Ziel...\n\ndie Schlangen-Höhle...\n\nund gehen hinein...\n\n"]},
                        {"Antworten": ["\nDer Eingang zur Höhle ist stockfinster,\nalso holen Sie ihre Fackel heraus und beschreiten den Weg weiter in die Höhle\nbis Sie zu einer Art großen Halle gelangen, die durch ein Loch in der Decke erhellt wird\nund dort ersichten Sie auch wovon der zwielichtige Mann sprach...\nein Sumpfgrottendrache...\nSie denken sich 'na großartig, wo hat mich dieser verdammte Drecksack nur herein geraten...'.\nAls der Drache Sie entdeckt, sagt er:\nDu Wicht, du wagst es dich in mein Heim zu begeben?! Was will so ein Wurm wie du von mir?...\nSie überlegen was Sie nun tun sollen und kommen nur auf zwei Lösungen um hier wieder lebend rauszukommen...\nZum einen könnten Sie versuchen sich irgendwie aus der ganzen Sache herauszureden,\nzum anderen könnten Sie versuchen ihn zu erschlagen...\n\n"]},
                        {"Antworten": [f"\nSie haben sich entschieden mit dem Drachen zu reden.\n\nSie: Ich wurde geschickt von einen zwielichtigen Mann in einer schwarzen Robe mit einem roten Emblem\num dich zu erschlagen und ihm etwas zurück zu bringen, dass du ihm getsohlen hast!\n\nDrache: Dieser Scharlatan schickt schon wieder jemanden der mich meines Besitz beraubt...\naber wieso versuchst du es nicht?\n\nSie: Ich dachte mir, warum sollte ich gegen so ein mächtiges Wesen kämpfen und sterben,\nwo ich nicht einmal weiß um was für einen Gegendstand es sich überhaupt handelt...\n\nDrache: Hahahaha...nicht einmal das hat er dir gesagt?\nDann werde ich dich aufklären und zwar hatte er eins meiner Eier gestohlen...\nIch konnte es aber wiedererlangen und seit dem versucht er wieder an eins von ihnen gelangen...\n\nSie: Widerwertiger Mistkerl...hätte er mir das von vornherein gesagt, wäre ich gar nicht erst gegangen...\n\nDrache: Also willst du mich nicht meines Nachwuchs berauben?\n\nSie: Nein, ich werde nach Hause gehen und diesem Bastard vorher noch einen Besuch abstatten!\n\nDrache: Dann habe dank Fremder und mögest du gut heimkehren...Lebewohl!\n\nSie: Ich hoffe du kannst nachdem ich mit 'ihm' fertig bin hier weiter in Ruhe leben!\n\nAchja mein Name ist {Name}, Lebewohl!\n\nErzähler: Und somit begeben Sie sich auf die Heimreise...\nAls Sie wieder zur Stadt kommen, wartet der zwielichtige Mann bereits auf Sie...\n\nZwielichtiger Mann: Und wie ist es gelaufen? Haben Sie das Ungetüm beseitigt?\n\nSie: Nein, keineswegs und der einzige der hier beseitigt werden muss, bist DU!\n\nErzähler: Sie ziehen ihr Schwert und weiden diesen miesen 'Sack voll von Trollscheiße' aus\nund lassen seine Leiche den Krähen zum Fraß und verrotten...\nMit dieser Genugtuhung gehen Sie wieder nach Hause und leben ihr Leben in Frieden...\n\nEnde.\n",
                                        "\nSie haben sich entschiedenden Drachen zu erschlagen.\nSie greifen den Drachen an und schlagen mit Ihrem Schwert zu,\ndie Haut ist allerdings zu hart und Ihr Schwert zerbricht...\n\nDer Drache schleudert Sie mit seinem Schwanz durch die gesamte Halle und gegen die Wand auf der anderen Seite.\nIhre Rüstung zerbarrst und Ihnen wurden viele Knochen gebrochen...\n\nSie sind nicht mehr in der Lage sich zu bewegen als der Drache auf Sie zu stampft...\nabsolut benommen nehmen Sie gerade noch wahr wie der Drache Sie hoch nimmt,\nbevor er Ihnenmit einem Biss Ihren Kopf vom Körper trennt und dann verschlingt...\n\nGame Over!\n\n"]}
                    ]    
    #endregion
    
#region Quest Anfang
    Anfang1 = "\nSo jetzt können wir richtig anfangen...\n\nIhr Abenteuer beginnt im Königreich Peithorn...\nWährend Sie sich in der nächst gelegenden Taverne ordentlich einen hinter den Helm römern,\nwerden Sie von einem zwielichtigen Mann in einer schwarzen Robe mit einem roten Emblem angesprochen...\n"
    TextOutputIntervall(Anfang1)
    # time.sleep(0.5)
    Gespräch1 = "\nZwielichtiger Typ: Hallo Fremder, ich hätte da eine bitte an euch...und zwar hätte ich eine Quest für Sie.\n\nEntscheiden Sie sich:\n"
    TextOutputIntervall(Gespräch1)
    
    # time.sleep(0.5)
    
    frage1 = "\n1. Lass hören, ich bin für alles bereit!\n2. Verschwinde du elendige Kanalratte!\n\n"
    TextOutputIntervall(frage1)
    AntwortFrage1 = input("\n")
    
    if AntwortFrage1 == "1":
        Antwort1 = "\nIn Ordnung, es geht sich um folgendes.\nIch bräuchte jemanden der für mich ein Monster beseitigt und mir etwas besorgt,\ndass es mir gestohlen hat. Sie finden es in der Schlangen-Höhle auf der anderen Seite von Peithorn.\nIch würde Sie auch reichlich entlohnen...\n"
        TextOutputIntervall(Antwort1)
    elif AntwortFrage1== "2":
        Antwort2 = "\nSie haben sich dafür entschieden das Abenteuer nicht anzunehmen...damit endet es hier...\n\nGame Over!\n"
        TextOutputIntervall(Antwort2)
        break
    else: 
        Antwort3 = "\nUngültige Eingabe...Spiel beendet..."
        TextOutputIntervall(Antwort3)
        break
    
    #endregion

#region Beginn Reise Wald/Gebirge

    UngültigeEingabe = "Ungültige Eingabe...Game Over!\n\n"

    TextOutputIntervall(Auswahlliste[0]["Frage"])
    TextOutputIntervall(Auswahlliste[0]["Antworten"])

    Eingabe1 = input("\n")

    if Eingabe1 == "1":
        TextOutputIntervall(Antwortenliste[0]["Antworten"][0]) #<== Auswahl Gebirge
    elif Eingabe1 == "2":
        TextOutputIntervall(Antwortenliste[0]["Antworten"][1]) #<== Auwahl Wald
    else:
        TextOutputIntervall(UngültigeEingabe)

    #endregion


#region Gebirge zu Sumpf zu Höhle/nach Hause
    if Eingabe1 == "1": 
        TextOutputIntervall(Auswahlliste[1]["Frage"])
        TextOutputIntervall(Auswahlliste[1]["Antworten"])

        Eingabe2 = input("\n\n")

        if Eingabe2 == "1":
            TextOutputIntervall(Antwortenliste[1]["Antworten"][0]) #<== Auswahl Gebirge
            TextOutputIntervall(Auswahlliste[2]["Frage"])
            TextOutputIntervall(Auswahlliste[2]["Antworten"]) 
            
            Eingabe3 = input("\n\n")
            
            if Eingabe3 == "1":
                TextOutputIntervall(Antwortenliste[2]["Antworten"][0]) #<== Auswahl Troll
            elif Eingabe3 == "2":
                TextOutputIntervall(Antwortenliste[2]["Antworten"][1])
                TextOutputIntervall(Auswahlliste[6]["Frage"])
                TextOutputIntervall(Auswahlliste[6]["Antworten"])
        
                Eingabe8 = input("\n\n")
        
                if Eingabe8 == "1":
                    TextOutputIntervall(Antwortenliste[7]["Antworten"][0]) #<== Auswahl Sumpf
                elif Eingabe8 == "2":
                    TextOutputIntervall(Antwortenliste[7]["Antworten"][1])
                elif Eingabe8 == "3":
                    TextOutputIntervall(Antwortenliste[7]["Antworten"][2])
                    TextOutputIntervall(Antwortenliste[8]["Antworten"][0])
                    TextOutputIntervall(Auswahlliste[7]["Frage"])
                    TextOutputIntervall(Auswahlliste[7]["Antworten"])
            
                    Eingabe12 = input("\n\n")
            
                    if Eingabe12 == "1":
                        TextOutputIntervall(Antwortenliste[9]["Antworten"][0]) #<== Auswahl Höhle
                    elif Eingabe12 == "2":
                        TextOutputIntervall(Antwortenliste[9]["Antworten"][1])
                    else:
                        TextOutputIntervall(UngültigeEingabe)
                        
        elif Eingabe2 == "2":
            TextOutputIntervall(Antwortenliste[1]["Antworten"][1]) #<== Auswahl Tal
            TextOutputIntervall(Antwortenliste[6]["Antworten"][0])
            TextOutputIntervall(Auswahlliste[6]["Frage"])
            TextOutputIntervall(Auswahlliste[6]["Antworten"])
        
            Eingabe7 = input("\n\n")
        
            if Eingabe7 == "1":
                TextOutputIntervall(Antwortenliste[7]["Antworten"][0]) #<== Auwahl Sumpf
            elif Eingabe7 == "2":
                TextOutputIntervall(Antwortenliste[7]["Antworten"][1])
            elif Eingabe7 == "3":
                TextOutputIntervall(Antwortenliste[7]["Antworten"][2])
                TextOutputIntervall(Antwortenliste[8]["Antworten"][0])
                TextOutputIntervall(Auswahlliste[7]["Frage"])
                TextOutputIntervall(Auswahlliste[7]["Antworten"])
            
                Eingabe11 = input("\n\n")
            
                if Eingabe11 == "1":
                    TextOutputIntervall(Antwortenliste[9]["Antworten"][0]) #<== Auswahl Höhle
                elif Eingabe11 == "2":
                    TextOutputIntervall(Antwortenliste[9]["Antworten"][1]) 
                else:
                    TextOutputIntervall(UngültigeEingabe)
        else:
            TextOutputIntervall(UngültigeEingabe)
            
        
    #endregion

#region Wald zu Sumpf zu Höhle/nach Hause

    if Eingabe1 == "2": 
        TextOutputIntervall(Auswahlliste[3]["Frage"]) 
        TextOutputIntervall(Auswahlliste[3]["Antworten"])     

        Eingabe4 = input("\n\n")
    
        if Eingabe4 == "1":
            TextOutputIntervall(Antwortenliste[3]["Antworten"][0]) #<== Auswahl Hexenhaus
            TextOutputIntervall(Auswahlliste[4]["Frage"])
            TextOutputIntervall(Auswahlliste[4]["Antworten"])
        
            Eingabe6 = input("\n\n")
    
            if Eingabe6 == "1":
                TextOutputIntervall(Antwortenliste[4]["Antworten"][0]) #<== Auswahl Hexe
                TextOutputIntervall(Antwortenliste[6]["Antworten"][0])
                TextOutputIntervall(Auswahlliste[6]["Frage"])
                TextOutputIntervall(Auswahlliste[6]["Antworten"])
        
                Eingabe10 = input("\n\n")
        
                if Eingabe10 == "1":
                    TextOutputIntervall(Antwortenliste[7]["Antworten"][0]) #<== Auswahl Sumpf
                elif Eingabe10 == "2":
                    TextOutputIntervall(Antwortenliste[7]["Antworten"][1])
                elif Eingabe10 == "3":
                    TextOutputIntervall(Antwortenliste[7]["Antworten"][2])
                    TextOutputIntervall(Antwortenliste[8]["Antworten"][0])
                    TextOutputIntervall(Auswahlliste[7]["Frage"])
                    TextOutputIntervall(Auswahlliste[7]["Antworten"])
            
                    Eingabe11 = input("\n\n")
            
                    if Eingabe11 == "1":
                        TextOutputIntervall(Antwortenliste[9]["Antworten"][0]) #<== Auswahl Höhle
                    elif Eingabe11 == "2":
                        TextOutputIntervall(Antwortenliste[9]["Antworten"][1])
                    else:
                        TextOutputIntervall(UngültigeEingabe)
                
            elif Eingabe6 == "2":
                TextOutputIntervall(Antwortenliste[4]["Antworten"][1])
            else:
                TextOutputIntervall(UngültigeEingabe)
        elif Eingabe4 == "2":
            TextOutputIntervall(Antwortenliste[3]["Antworten"][1]) #<== Auswahl Lichtung
            TextOutputIntervall(Auswahlliste[5]["Frage"])
            TextOutputIntervall(Auswahlliste[5]["Antworten"])
        
            Eingabe5 = input("\n\n")
        
            if Eingabe5 == "1":
                TextOutputIntervall(Antwortenliste[5]["Antworten"][0]) #<== Auswahl Tiefen des Waldes
                TextOutputIntervall(Antwortenliste[6]["Antworten"][0])
                TextOutputIntervall(Auswahlliste[6]["Frage"])
                TextOutputIntervall(Auswahlliste[6]["Antworten"])
        
                Eingabe9 = input("\n\n")
        
                if Eingabe9 == "1":
                    TextOutputIntervall(Antwortenliste[7]["Antworten"][0]) #<== Auswahl Sumpf
                elif Eingabe9 == "2":
                    TextOutputIntervall(Antwortenliste[7]["Antworten"][1])
                elif Eingabe9 == "3":
                    TextOutputIntervall(Antwortenliste[7]["Antworten"][2])
                    TextOutputIntervall(Antwortenliste[8]["Antworten"][0])
                    TextOutputIntervall(Auswahlliste[7]["Frage"])
                    TextOutputIntervall(Auswahlliste[7]["Antworten"])
            
                    Eingabe13 = input("\n\n")
            
                    if Eingabe13 == "1":
                        TextOutputIntervall(Antwortenliste[9]["Antworten"][0]) #<== Auswahl Höhle
                    elif Eingabe13 == "2":
                        TextOutputIntervall(Antwortenliste[9]["Antworten"][1])
                    else:
                        TextOutputIntervall(UngültigeEingabe)
                
            elif Eingabe5 == "2":
                TextOutputIntervall(Antwortenliste[5]["Antworten"][1])
        else:
            TextOutputIntervall(UngültigeEingabe)
        
    
    Ja_Nein = input("Möchtest du nocheinmal spielen? (1)ja\n\n") #<== Ende der While-Schleife
    
    if Ja_Nein == "1": 
        continue
    else: 
        break
            
    #endregion
#endregion
