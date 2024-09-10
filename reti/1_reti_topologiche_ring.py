''' 
 1: definiamo in maniera procedurale o OOP una serie di Computer con MAC e IP 
 2: definiamo alla stessa maniera un messaggio contenente IP del mittente e destinatario
 3: definiamo una funzione SEND che ricevuto un messaggio stampa tutti i MAC dei computer intermedi e infine messaggio e MAC del PC destinatario
 4: quali problematiche possono incorrere nel tuo codice? 
 5: quali problemi potrebbe avere questa struttura indipendentemente dal tuo codice? 
 6: se N è il numero di computer, nel caso migliore, peggiore e medio, quante operazioni vengono eseguite dalla funzione SEND?
 6.1: (con un'operazione si intende l'insieme di confronti/assegnazioni/etc svolte su un elemento)
'''

pc = { 
      "ip": 192168001012,
      "mac": "asd43f434rfd",
    
    }
pc2 = { 
      "ip": 192168001144,
      "mac": "bas43f434rfd",
    }
pc3 = { 
      "ip": 192168001200,
      "mac": "cic43f434rfd",
    }

pc["next"] = pc2
pc2["next"] = pc3
pc3["next"] = pc

msg = {
  "ip1":  192168001012,
  "ip2":  192168001200,
  "payload": "ciao ti ho trovato",
}



# simuliamo una rete ad anello
def sendRING(messaggio):
     found = False
     curr = pc 
    
     while(not found):
      
       if(curr["ip"] == messaggio["ip2"]):
         found = True
       else:
         curr = curr["next"]
         print("il messaggio è stato inoltrato dal PC di MAC"+curr["mac"])
     print("il PC di MAC "+curr["mac"]+" ha ricevuto il messaggio"+messaggio["payload"])
     
    
        
    
sendRING(msg)
   