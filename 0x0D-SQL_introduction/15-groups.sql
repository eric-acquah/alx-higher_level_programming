-- Display score grouped by frequency
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score ORDER BY score DESC;
