-- Création de la table des continents
CREATE OR REPLACE TABLE football.continents (
  area_id INT64,
  area_name STRING,
  area_code STRING
);

-- Création de la table des compétitions
CREATE OR REPLACE TABLE football.competitions (
  id INT64,
  name STRING,
  type STRING,
  code STRING,
  area_id INT64,
  plan STRING,
  currentSeason_id STRING,
  numberOfAvailableSeasons STRING
);

-- Création de la table des saisons associées aux compétitions
CREATE OR REPLACE TABLE football.saisons (
    id INT64,
    competition_id INT64,
    start_date DATE,
    end_date DATE,
    current_matchday INT64,
    winner STRING
);
