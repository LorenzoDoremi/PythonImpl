'''
esercizio: ARP/IP su una rete a stella



'''
class Device():
    def __init__(self,ip,mac) -> None:
        self.ip = ip
        self.mac = mac 
        self.arp_table = []
    # invia un messaggio tramite un router
    def send(self, dest_ip,dest_mac, router):
        router.receive(self, dest_ip,dest_mac)
        
    # riceve un messaggio da un router
    def receive(self,dest_ip,dest_mac,payload):
         # il messaggio mi riguarda ed è per ARP
         if(dest_ip == self.ip and dest_mac == "ff:ff:ff:ff:ff"):
              return {"mac": self.mac,"arp": True}
         elif(dest_ip == self.ip):
               #ho ricevuto un mac e un ip di un computer
               if(payload and payload["mac"] and payload["ip"]):
                   self.arp_table.append({"mac": payload["mac"], "ip":payload["ip"]})
                   return {"answer": "ricevuto","arp": False}
               else: 
                   print("ho ricevuto un messaggio")
         else:
             return False
             
        
             
             
            
class Router(Device):
    def __init__(self, ip, mac) -> None:
        super().__init__(ip, mac)
        self.devices = []
    def receive(self,sender, ip,mac):
        #arp: mando a tutti 
        requested_mac = ""
        if(mac == "ff:ff:ff:ff:ff"):
            # chiedi risposta a tutti i device
            for device in self.devices:
                answer = device.receive(ip,mac,{})
                # se uno ha risposto con i suoi dati
                if(answer):
                    requested_mac = answer["mac"]
            sender.receive(sender.ip, sender.mac,{"mac": requested_mac,"ip":ip})
                
        # messaggio normale
        else: 
            for device in self.devices: 
                if(device.ip == ip):
                    device.receive(ip,self, {})
        
                
               
    
pc1 = Device("192.168.1.1","aa:aa:aa:bb:22")
pc2 = Device("192.168.1.5","ab:aa:aa:bb:55")
pc3 = Device("192.168.1.8","ac:aa:aa:bb:99")
router =Router("192.168.1.254","rr:rr:rr:rr:rr")
router.devices = [pc1,pc2,pc3]
pc1.send("192.168.1.5","ff:ff:ff:ff:ff", router)
pc1.send("192.168.1.8","ab:aa:aa:bb:55", router)

print(pc1.arp_table)    
    




