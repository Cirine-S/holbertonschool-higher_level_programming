-- displays the max temperature of each state (ordered by State name)

SELECT state, max(value) as max_temp
FROM temperatures
ORDER BY state
LIMIT 3;