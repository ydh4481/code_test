select a.id,
    case 
        when a.per <= 0.25 then 'CRITICAL'
        when a.per <= 0.5 then 'HIGH'
        when a.per <= 0.75 then 'MEDIUM'
        else 'LOW' 
    end COLONY_NAME
from (
    select id, 
        PERCENT_RANK() over (order by SIZE_OF_COLONY desc) per
    from ECOLI_DATA 
) a
order by id;