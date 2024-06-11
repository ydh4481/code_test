-- 코드를 입력하세요
WITH ins_intact AS (
    SELECT
        animal_id
    FROM animal_ins
    WHERE sex_upon_intake like 'Intact%'
)

select ao.animal_id,
    ao.animal_type,
    ao.name
from animal_outs ao
join ins_intact ii on ao.animal_id=ii.animal_id
where ao.sex_upon_outcome not like 'Intact%'