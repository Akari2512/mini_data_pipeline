-- Average electricity bill per person
SELECT
    COUNT(*) as households,
    AVG(amount_paid) as avg_bill,
    AVG(bill_per_person) as avg_bill_per_person
FROM electricity_bills
GROUP BY num_people
ORDER BY num_people;

-- Average electricity bill per square foot
SELECT
    CASE 
        WHEN housearea < 500 THEN 'Less than 500 sqft'
        WHEN housearea BETWEEN 500 AND 1000 THEN '500 to 1000 sqft'
        ELSE 'More than 1000 sqft'
    END as house_size_group,
    COUNT (*) as households,
    AVG(bil_per_sqft) as avg_bill_per_sqft
FROM electricity_bills
GROUP BY
    CASE 
        WHEN housearea < 500 THEN 'Less than 500 sqft'
        WHEN housearea BETWEEN 500 AND 1000 THEN '500 to 1000 sqft'
        ELSE 'More than 1000 sqft'
    END
ORDER BY house_size_group;

-- Comparison of average bills in urban vs rural areas
SELECT
    is_urban,
    COUNT(*) AS households,
    AVG(amount_paid) AS avg_bill,
    AVG(bil_per_sqft) AS avg_bill_per_sqft
FROM electricity_bills
GROUP BY is_urban;

-- Effect of number of children on electricity bills
SELECT
    num_children,
    COUNT(*) AS households,
    AVG(amount_paid) AS avg_bill
FROM electricity_bills
GROUP BY num_children
ORDER BY num_children;

