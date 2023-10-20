-- Displays the 3 cities with the highest average temperatures between July and August.
SELECT `city`, AVG(`value`) AS `temp_avg`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `temp_avg` DESC
LIMIT 3;
