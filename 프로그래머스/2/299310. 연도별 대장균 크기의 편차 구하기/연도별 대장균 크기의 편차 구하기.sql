-- 코드를 작성해주세요
with year_max as (
select year(differentiation_date) as year,
    max(size_of_colony) as year_max_size
from ecoli_data
group by year
)
select 
    t.year,
    t.year_max_size - s.size_of_colony as year_dev,
    s.id
from ecoli_data s
left join year_max t on year(s.differentiation_date) = t.year
order by 1, 2