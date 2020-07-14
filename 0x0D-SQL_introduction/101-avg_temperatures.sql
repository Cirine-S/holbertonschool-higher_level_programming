-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)

SELECT city, avg(value) as avg_temp
FROM temperatures
ORDER BY AVG(value) DESC;