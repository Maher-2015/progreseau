from netmiko import ConnectHandler
import time

# Paramètres d'accès du routeur
router = {
    'device_type': 'cisco_ios',
    'host': 'sandbox-iosxe-latest-1.cisco.com',
    'username': 'admin',
    'password': 'C1sco12345',
    'port': 22,  # SSH port
    'secret': 'C1sco12345',  # Le mot de passe enable (si nécessaire)
}

# Connexion au routeur
net_connect = ConnectHandler(**router)
net_connect.enable()  # Entrer en mode enable

# 1) Afficher la date côté routeur (show clock)
output_clock = net_connect.send_command('show clock')
print("Date et heure du routeur:")
print(output_clock)

# 2) Afficher les interfaces du routeur dans un fichier interfaces.txt
output_interfaces = net_connect.send_command('show ip interface brief')
with open('interfaces.txt', 'w') as file:
    file.write(output_interfaces)
print("Les interfaces ont été enregistrées dans le fichier 'interfaces.txt'.")

# 3) Configurer une interface Loopback
config_commands = [
    'interface loopback0',       # Passer en mode configuration de l'interface Loopback0
    'ip address 10.8.8.8 255.255.255.240',  # Définir l'adresse IP
    'no shutdown',               # Activer l'interface
]

# Envoi des commandes de configuration
net_connect.send_config_set(config_commands)
print("L'interface loopback0 a été configurée avec l'adresse IP 10.8.8.8/28.")

# Fermer la connexion
net_connect.disconnect()