SELECT r.name FROM students s
JOIN rooms r
ON r.id=s.room
GROUP BY r.id,r.name 
HAVING
COUNT(CASE WHEN sex='M' THEN 1 END)>0 AND 
COUNT(CASE WHEN sex='F' THEN 1 END)>0
ORDER BY r.id;