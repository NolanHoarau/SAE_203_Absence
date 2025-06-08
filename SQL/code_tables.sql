CREATE DATABASE IF NOT EXISTS gestion_absence
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
USE gestion_absence;

-- 1. Table des enseignants
CREATE TABLE enseignants (
    id_enseignant SERIAL PRIMARY KEY,
    nom_enseignant VARCHAR(100) NOT NULL,
    prenom_enseignant VARCHAR(100) NOT NULL,
    email_enseignant VARCHAR(150) NOT NULL UNIQUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2. Table des cours
CREATE TABLE cours (
    id_cours SERIAL PRIMARY KEY,
    titre_cours VARCHAR(150) NOT NULL,
    date_cours DATE NOT NULL,
    enseignant_cours INT NOT NULL,
    durée_cours INTERVAL NOT NULL,
    groupe_cours INT,
    FOREIGN KEY (enseignant_cours) REFERENCES enseignants(id_enseignant)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 3. Table des groupes d'étudiants
CREATE TABLE `groupes_d_etudiants` (
    id_groupe SERIAL PRIMARY KEY,
    id_cours INT NOT NULL,
    nom_groupe VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_cours) REFERENCES cours(id_cours)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 4. Table des étudiants
CREATE TABLE etudiants (
    id_etudiant SERIAL PRIMARY KEY,
    id_groupe INT,
    nom_etudiant VARCHAR(100) NOT NULL,
    prenom_etudiant VARCHAR(100) NOT NULL,
    email_etudiant VARCHAR(150) NOT NULL UNIQUE,
    groupe_etudiants VARCHAR(100),
    photo_etudiant BYTEA,
    FOREIGN KEY (id_groupe) REFERENCES groupes_d_etudiants(id_groupe)
        ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 5. Table des absences aux cours
CREATE TABLE absences_cours (
    id_absence_cours SERIAL PRIMARY KEY,
    id_cours INT NOT NULL,
    id_enseignant INT NOT NULL,
    id_etudiant INT NOT NULL,
    justifie BOOLEAN DEFAULT FALSE,
    justification TEXT,
    FOREIGN KEY (id_cours) REFERENCES cours(id_cours)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_enseignant) REFERENCES enseignants(id_enseignant)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_etudiant) REFERENCES etudiants(id_etudiant)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
