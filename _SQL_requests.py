#Задание №1:
SELECT login, COUNT("inDelivery")
FROM "Couriers" as c
JOIN "Orders" AS o ON c.id=o."courierId"
WHERE "inDelivery" = true
GROUP BY login;

#Задание №2:
SELECT track,
    CASE
        WHEN finished = true THEN 2
        WHEN cancelled = true THEN -1
        WHEN "inDelivery" = true THEN 1
        ElSE 0
    END as "order status"
FROM "Orders";
