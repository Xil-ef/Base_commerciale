-- Total de vente réalisé
SELECT
  sum(total) as nb_T
FROM Commandes
group by client_id
order by nb_T desc