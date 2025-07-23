-- les détails de chaque commande avec les noms de produits
SELECT
  DetailsCommande.commande_id,
  DetailsCommande.detail_id,
  DetailsCommande.prix_vente_unitaire,
  DetailsCommande.produit_id,
  DetailsCommande.quantite,
  Produits.nom_produit
FROM DetailsCommande
join Produits on DetailsCommande.produit_id=Produits.produit_id