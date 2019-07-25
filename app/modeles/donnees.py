from app import db


Images_has_Objets = db.Table("images_has_objets",
                             db.Column("Images_id_images", db.Integer, db.ForeignKey("images.id_image"),
                                       primary_key=True),
                             db.Column("Objets_id_objet", db.Integer, db.ForeignKey("objets.id_objet"),
                                       primary_key=True)
                             )

Images_has_Bibliographie = db.Table("images_has_bibliographie",
                                    db.Column("Images_id_images", db.Integer, db.ForeignKey("images.id_image"),
                                              primary_key=True),
                                    db.Column("Bibliographie_id_ouvrage", db.Integer,
                                              db.ForeignKey("bibliographie.id_ouvrage"), primary_key=True),
                                    db.Column("pages", db.String),
                                    db.Column("reference", db.String),
                                    db.Column("commentaire", db.String)
                                    )

Objets_has_Bibliographie = db.Table("objets_has_bibliographie",
                                    db.Column("Objets_id_objet", db.Integer, db.ForeignKey("objets.id_objet"),
                                              primary_key=True),
                                    db.Column("Bibliographie_id_ouvrage", db.Integer,
                                              db.ForeignKey("bibliographie.id_ouvrage"), primary_key=True),
                                    db.Column("pages", db.String),
                                    db.Column("reference", db.String),
                                    db.Column("numero_catalogue", db.String),
                                    db.Column("commentaire", db.String),
                                    db.Column("url", db.String)
                                    )

Personnes_has_Bibliographie = db.Table("personnes_has_bibliographie",
                                       db.Column("Personnes_id_personne", db.Integer,
                                                 db.ForeignKey("personnes.id_personne"), primary_key=True),
                                       db.Column("Bibliographie_id_ouvrage", db.Integer,
                                              db.ForeignKey("bibliographie.id_ouvrage"), primary_key=True),
                                       db.Column("pages", db.String),
                                       db.Column("url", db.String)
                                       )


Collections_has_Bibliographie = db.Table("collections_has_bibliographie",
                                         db.Column("Collections_id_collection", db.Integer,
                                                   db.ForeignKey("collections.id_collection"), primary_key=True),
                                         db.Column("Bibliographie_id_ouvrage", db.Integer,
                                                   db.ForeignKey("bibliographie.id_ouvrage"), primary_key=True),
                                         db.Column("pages", db.String),
                                         db.Column("url", db.String)
                                         )


Objets_has_Archives = db.Table("objets_has_archives",
                               db.Column("Objets_id_objet", db.Integer, db.ForeignKey("objets.id_objet"),
                                         primary_key=True),
                               db.Column("Archives_id_archive", db.Integer, db.ForeignKey("archives.id_archive"),
                                         primary_key=True),
                               db.Column("reference", db.String)
                               )


Voyages_Navires = db.Table("voyage_navire",
                           db.Column("Navires_id_navire", db.Integer, db.ForeignKey("Navires.id_navire"),
                                     primary_key=True),
                           db.Column("Lieux_depart", db.Integer, db.ForeignKey("lieux.id_lieu"), primary_key=True),
                           db.Column("Lieux_arrivee", db.Integer, db.ForeignKey("lieux.id_lieu"), primary_key=True),
                           db.Column("date_depart", db.String),
                           db.Column("date_arrivee", db.String),
                           db.Column("chargement", db.String)
                           )


# Table des objets
# Classe centrale de la bdd
class Objets(db.Model):
    __tablename__ = "objets"
    id_objet = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    type_objet = db.Column(db.String)
    matiere = db.Column(db.String)
    inscription = db.Column(db.String)
    description_Fauvel = db.Column(db.String)
    autre_description = db.Column(db.String)
    description_moderne = db.Column(db.String)
    chronologie_generique = db.Column(db.String)
    datation_moderne = db.Column(db.String)
    ref_inscription = db.Column(db.String)
    inscription_cahier_Fauvel = db.Column(db.String)
    decouverte_av_dec_1792 = db.Column(db.String)
    date_decouverte = db.Column(db.String)
    lieu_decouverte = db.Column(db.Integer, db.ForeignKey("id_lieu"))
    lieu_decouverte_detail = db.Column(db.String)
    acquisition = db.Column(db.String)
    mode_acquisition = db.Column(db.String)
    autorisation = db.Column(db.String)
    detruit = db.Column(db.Numeric)
    commentaire = db.Column(db.String)

    image_objet = db.relationship("Images", secondary=Images_has_Objets, back_populates="objet_image")
    bibliographie_objet = db.relationship("Bibliographie", secondary=Objets_has_Bibliographie,
                                          back_populates="objet_bibliographie")
    archive_objet = db.relationship("Archives", secondary=Objets_has_Archives, back_populates="objet_archive")


# Table des lieux
class Lieux(db.Model):
    __tablename__ = "lieux"
    id_lieu = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    coordonnees = db.Column(db.String)
    pays = db.Column(db.String)
    region = db.Column(db.String)
    ville = db.Column(db.String)
    secteur = db.Column(db.String)
    details = db.Column(db.String)

    lieu_decouverte = db.relationship("Objets", back_populates="Lieux")
    navire_lieu = db.relationship("Navires", secondary=Voyages_Navires, back_populates="lieu_navire")


# Table des personnes
class Personnes(db.Model):
    __tablename__ = "personnes"
    id_personne = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    nom_prenom = db.Column(db.String)
    date_naissance = db.Column(db.String)
    date_mort = db.Column(db.String)
    voyageur = db.Column(db.Numeric)
    collectionneur = db.Column(db.Numeric)
    conservateur = db.Column(db.Numeric)
    emissaire = db.Column(db.Numeric)
    autre = db.Column(db.String)
    connu_Fauvel = db.Column(db.Numeric)
    acheteur_direct = db.Column(db.Numeric)

    bibliographie_personne = db.relationship("Bibliographie", secondary=Personnes_has_Bibliographie,
                                             back_populates="personne_bibliographie")


# Table des images
class Images(db.Model):
    __tablename__ = "images"
    id_image = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    reference = db.Column(db.String)
    chemin_image = db.Column(db.String)

    objet_image = db.relationship("Objets", secondary=Images_has_Objets, back_populates="image_objet")
    bibliographie_image = db.relationship("Bibliographie", secondary=Images_has_Bibliographie,
                                          back_populates="image_bibliographie")


# Table des collections
class Collections(db.Model):
    __tablename__ = "collections"
    id_collection = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    nom_collection = db.Column(db.String)
    collectionneur = db.Column(db.Integer)
    description = db.Column(db.String)
    lieu_conservation = db.Column(db.Integer)

    bibliographie_collection = db.relationship("Bibliographie", secondary=Collections_has_Bibliographie,
                                               back_populates="collection_bibliographie")

# Table de la bibliographie
class Bibliographie(db.Model):
    __tablename__ = "bibliographie"
    id_ouvrage = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    reference_complete = db.Column(db.String)
    url = db.Column(db.String)
    catalogue_vente = db.Column(db.Numeric)

    image_bibliographie = db.relationship("Images", secondary=Images_has_Bibliographie,
                                          back_populates="bibliographie_image")
    objet_bibliographie = db.relationship("Objets", secondary=Objets_has_Bibliographie,
                                          back_populates="bibliographie_objet")
    personne_bibliographie = db.relationship("Personnes", secondary=Personnes_has_Bibliographie,
                                             back_populates="bibliographie_personne")
    collection_bibliographie = db.relationship("Collections", secondary=Collections_has_Bibliographie,
                                               back_populates="bibliographie_colletion")


# Table des archives
class Archives(db.Model):
    __tablename__ = "archives"
    id_archive = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    reference = db.Column(db.String)
    institution_conservation = db.Column(db.String)
    numero_inventaire = db.Column(db.String)
    auteur = db.Column(db.String)
    titre = db.Column(db.String)
    date = db.Column(db.String)

    objet_archive = db.relationship("Objets", secondary=Objets_has_Archives, back_populates="archive_objet")


# Table des navires
class Navires(db.Model):
    __tablename__ = "navires"
    id_navire = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    nom = db.Column(db.String)
    capitaine = db.Column(db.Integer)
    commentaire = db.Column(db.String)

    lieu_navire = db.relationship("Lieux", secondary=Voyages_Navires, back_populates="navire_lieu")


# Table géographique : les étapes et les collections liées aux objets à un instant T
class Etapes_et_Collections(db.Model):
    __tablename__ = "etapes_et_collections"
    id_etape = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    objet = db.Column(db.Integer)
    collection = db.Column(db.Integer)
    lieu_etape = db.Column(db.Integer)
    date = db.Column(db.String)
    emissaire = db.Column(db.Integer)
    navire = db.Column(db.Integer)
    commentaire = db.Column(db.String)


