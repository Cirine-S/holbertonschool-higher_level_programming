-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)

SELECT city, avg_temp
FROM temperatures
ORDER BY avg_temp DESC;