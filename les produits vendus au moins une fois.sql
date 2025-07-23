-- les produits vendus au moins une fois
SELECT
  Produits.produit_id,
  Produits.nom_produit
FROM Produits
where 
  EXISTS (select 1 from DetailsCommande where DetailsCommande.produit_id=Produits.produit_id)