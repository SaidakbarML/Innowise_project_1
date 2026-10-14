SELECT
	ROUND(AVG(EXTRACT (EPOCH FROM (NOW()-s.birthday)))/31536000,2) AS avg_age,
	r.name
	FROM students s
	JOIN rooms r 
	ON r.id=s.room
GROUP BY r.id, r.name
ORDER BY avg_age,r.id ASC 
LIMIT 5;