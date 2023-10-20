-- Displays the average temperature (in Fahrenheit) by city, ordered by descending temperature.
SELECT `city`, AVG(`value`) AS `temp_avg`
FROM `temperatures`
GROUP BY `city`
ORDER BY `temp_avg` DESC;
