-- View sample records from processed product data
SELECT *
FROM mydatabase.product
LIMIT 10;

-- Daily summary report: total number of records
SELECT
  COUNT(*) AS total_records
FROM mydatabase.product;
