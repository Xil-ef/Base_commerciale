--toutes les commandes avec le nom du client
SELECT
  Commandes.commande_id,
  Clients.nom,
  Commandes.date_commande
from Commandes
join Clients on Commandes.client_id=Clients.client_id