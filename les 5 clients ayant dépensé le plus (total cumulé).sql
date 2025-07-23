-- Trouver les 5 clients ayant dépensé le plus (total cumulé)
SELECT
  Clients.client_id,
  Clients.nom,
  sum(Commandes.total) as total_commande
from Clients
join Commandes on Clients.client_id=Commandes.client_id
group by Clients.client_id
order by total_commande desc
limit 5