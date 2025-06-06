-- 코드를 작성해주세요
WITH RARE AS (
    SELECT ITEM_ID
    FROM ITEM_INFO II
    WHERE RARITY = 'RARE'
),
NEXT_ITEM AS (
    SELECT ITEM_ID
    FROM ITEM_TREE
    WHERE PARENT_ITEM_ID IN (
        SELECT ITEM_ID
        FROM RARE
    )
)
SELECT ITEM_ID,
    ITEM_NAME,
    RARITY
FROM ITEM_INFO
WHERE ITEM_ID IN (
    SELECT ITEM_ID
    FROM NEXT_ITEM
)
ORDER BY ITEM_ID DESC
;
