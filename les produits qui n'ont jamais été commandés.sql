-- les produits qui n'ont jamais été commandés
SELECT
  Produits.produit_id,
  Produits.nom_produit
FROM Produits
where 
  NOT EXISTS (select 1 from DetailsCommande where DetailsCommande.produit_id=Produits.produit_id)