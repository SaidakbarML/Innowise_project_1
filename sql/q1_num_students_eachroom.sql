select r."name" ,count(r.id) as num_students
from students s 
join rooms r 
on r.id=s.room 
group by r.id
order by num_students;