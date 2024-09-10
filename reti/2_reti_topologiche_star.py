'''
esercizio: ARP/IP su una rete a stella
si definiscano dei computer dotati di MAC e IP
si definisca un ROUTER/SWITCH, dotato anch'esso di MAC e IP
si definisca un messaggio contenente IP di mittente e destinatario
si definisca una funzione che permetta al router di far combaciare IP e MAC dei vari computer
si definisca una funzione SEND che permette di inviare il messaggio al MAC corretto 
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

router = {
     "ip": 0,
      "mac": "0",
      "table": []
}

def arp(mittente, richiesta, router):
     
    # vedo se inserire il nuovo MAC
    mac = None 
    cached = False
    for record in router["table"]:
        if(richiesta == record["ip"]):
            mac = record["mac"]
        if(mittente["ip"] == record["ip"]):
             cached = True
    if( not cached):
        router["table"].append({"ip": mittente["ip"],"mac": mittente["mac"]})
    
    if(not mac):
        # chiedi a tutti i computer quale è il loro IP/MAC o aspetta.
        print("wait")
    else:
        print("MAC di",richiesta," = ",mac)
    

arp(pc,192168001200,router)
arp(pc3,192168001012,router)
arp(pc,192168001200,router) 
    
    




