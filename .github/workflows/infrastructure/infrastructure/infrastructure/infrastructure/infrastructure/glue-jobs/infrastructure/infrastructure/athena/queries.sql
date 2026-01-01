-- View sample records from product data
SELECT *
FROM product
LIMIT 10;

-- Daily summary report: total number of records
SELECT
  COUNT(*) AS total_records
FROM product;
