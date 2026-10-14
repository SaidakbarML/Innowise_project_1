SELECT r."name" ,COUNT(r.id) AS num_students
FROM students s 
LEFT JOIN rooms r 
ON r.id=s.room 
GROUP BY r.id
ORDER BY num_students;