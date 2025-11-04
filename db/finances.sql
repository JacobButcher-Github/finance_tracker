--TABLES
CREATE TABLE IF NOT EXISTS income (
  date DATE NOT NULL UNIQUE,
  gross NUMERIC(12, 2) NOT NULL,
  k401 NUMERIC(12, 2) NOT NULL,
  fed_tax NUMERIC(12, 2) NOT NULL,
  ss_tax NUMERIC(12, 2) NOT NULL,
  medicare_tax NUMERIC(12, 2) NOT NULL,
  state_tax NUMERIC(12, 2) NOT NULL,
  other_income NUMERIC(12, 2) NOT NULL,
  net_income NUMERIC(12, 2) NOT NULL,
  total_tax NUMERIC(12, 2) NOT NULL,
  tax_percent_income DECIMAL(5, 2) CHECK (
    tax_percent_income <= 100
    AND tax_percent_income >= 0
  ),
  PRIMARY KEY (date)
);

CREATE TABLE IF NOT EXISTS expenditure (
  --Special in this table, can have multiple from the same date.
  id SERIAL UNIQUE,
  date DATE NOT NULL,
  category TEXT CHECK (LENGTH (category) < 100),
  amount NUMERIC(12, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS net (
  date DATE NOT NULL UNIQUE,
  checking NUMERIC(12, 2),
  savings NUMERIC(12, 2),
  ira NUMERIC(12, 2),
  k401 NUMERIC(12, 2),
  hsa NUMERIC(12, 2),
  asset_value NUMERIC(12, 2),
  asset_debt NUMERIC(12, 2),
  other_debt NUMERIC(12, 2),
  PRIMARY KEY (date)
);

CREATE TABLE IF NOT EXISTS house (
  id SERIAL UNIQUE,
  purchase_price NUMERIC(12, 2),
  down_payment NUMERIC(12, 2),
  finance_amount NUMERIC(12, 2),
  apr DECIMAL(2, 2) CHECK (
    apr < 99.1
    AND apr > 0
  ),
  years INTEGER,
  monthly NUMERIC(12, 2),
  total_interest NUMERIC(12, 2)
);

CREATE TABLE IF NOT EXISTS caps (
  date DATE NOT NULL UNIQUE,
  k401 NUMERIC(12, 2),
  ira NUMERIC(12, 2),
  hsa NUMERIC(12, 2),
  PRIMARY KEY (date)
);
