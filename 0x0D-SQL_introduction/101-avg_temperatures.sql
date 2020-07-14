-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)

SELECT city, avg(value) as avg_temp
FROM temperatures
GROUP BY AVG(value) DESC;