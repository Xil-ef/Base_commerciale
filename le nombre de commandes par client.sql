-- Afficher le nombre de commandes par client
SELECT
  Clients.client_id,
  Clients.nom,
  count(Commandes.commande_id) as nb_commande
from Clients
left join Commandes on Clients.client_id=Commandes.client_id
GROUP by Clients.client_id
order by nb_commande desc