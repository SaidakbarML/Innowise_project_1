SELECT r.name,ROUND(EXTRACT(EPOCH FROM (MAX(birthday)-MIN(birthday)))/31536000,2) AS diff_age FROM students s
JOIN rooms r
ON r.id=s.room
GROUP BY r.id,r.name
ORDER BY diff_age DESC
LIMIT 5;
