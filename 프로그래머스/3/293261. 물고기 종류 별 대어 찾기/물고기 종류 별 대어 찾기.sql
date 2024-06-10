-- 코드를 작성해주세요

select fi.id,
    fni.fish_name,
    fi.length
from fish_info fi
left join fish_name_info fni on fi.fish_type=fni.fish_type
where (fi.fish_type, length) in (
    select fish_type,
        max(length) length
    from fish_info
    group by fish_type
)