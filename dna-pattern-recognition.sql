-- https://leetcode.com/problems/dna-pattern-recognition/description/
-- beats 64% runtime

CREATE TEMPORARY TABLE Samples (
    sample_id INT,
    dna_sequence VARCHAR(255),
    species VARCHAR(100),
    PRIMARY KEY (sample_id)
);

INSERT INTO Samples (sample_id, dna_sequence, species) values
    ('1', 'ATGCTAGCTAGCTAA', 'Human'),
    ('2', 'GGGTCAATCATC', 'Human'),
    ('3', 'ATATATCGTAGCTA', 'Human'),
    ('4', 'ATGGGGTCATCATAA', 'Mouse'),
    ('5', 'TCAGTCAGTCAG', 'Mouse'),
    ('6', 'ATATCGCGCTAG', 'Zebrafish'),
    ('7', 'CGTATGCGTCGTA', 'Zebrafish');


SELECT
    sample_id,
    dna_sequence,
    species,
    IF(dna_sequence LIKE 'ATG%', 1, 0) has_start,
    IF(SUBSTRING(dna_sequence, -3) IN ('TAA', 'TAG', 'TGA'), 1, 0) has_stop,
    IF(dna_sequence LIKE '%ATAT%', 1, 0) has_atat,
    IF(dna_sequence LIKE '%GGG%', 1, 0) has_ggg
FROM
    Samples
ORDER BY
    sample_id

