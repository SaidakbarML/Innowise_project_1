select r.name,round(extract(epoch from (max(birthday)-min(birthday)))/31536000,2) as diff_age from students s
join rooms r
on r.id=s.room
group by r.name
order by diff_age desc
limit 5;
