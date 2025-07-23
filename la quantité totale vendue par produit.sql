-- Calculer la quantité totale vendue par produit
SELECT
  Produits.produit_id,
  Produits.nom_produit,
  count(DetailsCommande.produit_id) as q_total_vendu
FROM Produits
left join DetailsCommande on DetailsCommande.produit_id=Produits.produit_id
group by Produits.produit_id
order by q_total_vendu DESC