select r.name from students s
join rooms r
on r.id=s.room
group by r.id,r.name 
having
count(case when sex='M' then 1 end)>0 and 
count(case when sex='F' then 1 end)>0
order by r.id;