create database if not exists gestion_abscence
	character set utf8mb4
    collate utf8mb4_unicode_ci;
use gestion_abscence;

CREATE TABLE groupes (
  id INT NOT NULL AUTO_INCREMENT,
  nom VARCHAR(100) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

CREATE TABLE enseignants (
  id INT NOT NULL AUTO_INCREMENT,
  nom VARCHAR(50) NOT NULL,
  prenom VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  PRIMARY KEY (id)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;
  
CREATE TABLE etudiants (
  id INT NOT NULL AUTO_INCREMENT,
  nom VARCHAR(50) NOT NULL,
  prenom VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  groupe_id INT NOT NULL,
  photo VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY (id),
  INDEX idx_etudiants_groupe (groupe_id),
  CONSTRAINT fk_etudiants_groupe
    FOREIGN KEY (groupe_id) REFERENCES groupes(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

CREATE TABLE cours (
  id INT NOT NULL AUTO_INCREMENT,
  titre VARCHAR(200) NOT NULL,
  date DATE NOT NULL,
  enseignant_id INT NOT NULL,
  duree INT NOT NULL COMMENT 'Durée en minutes',
  groupe_id INT NOT NULL,
  PRIMARY KEY (id),
  INDEX idx_cours_enseignant (enseignant_id),
  INDEX idx_cours_groupe (groupe_id),
  CONSTRAINT fk_cours_enseignant
    FOREIGN KEY (enseignant_id) REFERENCES enseignants(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  CONSTRAINT fk_cours_groupe
    FOREIGN KEY (groupe_id) REFERENCES groupes(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;

CREATE TABLE absences (
  id INT NOT NULL AUTO_INCREMENT,
  etudiant_id INT NOT NULL,
  cours_id INT NOT NULL,
  justifie TINYINT(1) NOT NULL DEFAULT 0 COMMENT '0 = non justifié, 1 = justifié',
  justification TEXT DEFAULT NULL,
  date_enregistrement TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uk_absence_etudiant_cours (etudiant_id, cours_id),
  INDEX idx_absences_etudiant (etudiant_id),
  INDEX idx_absences_cours (cours_id),
  CONSTRAINT fk_absences_etudiant
    FOREIGN KEY (etudiant_id) REFERENCES etudiants(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT fk_absences_cours
    FOREIGN KEY (cours_id) REFERENCES cours(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci;
