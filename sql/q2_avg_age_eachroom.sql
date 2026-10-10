select
	round(avg(extract (epoch from (now()-s.birthday)))/31536000,2) as avg_age,
	r.name
	from students s
	join rooms r 
	on r.id=s.room
group by r.id, r.name
order by avg_age,r.id asc 
limit 5;