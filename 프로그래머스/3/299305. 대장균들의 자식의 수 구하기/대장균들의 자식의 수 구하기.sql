-- 코드를 작성해주세요
with son as (
    select parent_id,
        count(*) as child_count
    from ecoli_data
    where parent_id is not null
    group by parent_id
)

select e.id,
    ifnull(son.child_count, 0) as child_count
from ecoli_data e
left join son on e.id = son.parent_id
order by id