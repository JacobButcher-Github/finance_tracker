--TABLES
CREATE TABLE IF NOT EXISTS income (
  id UNIQUE SERIAL,
  date DATE NOT NULL,
  gross MONEY NOT NULL,
  k401 MONEY NOT NULL,
  fed_tax MONEY NOT NULL,
  ss_tax MONEY NOT NULL,
  medicare_tax MONEY NOT NULL,
  state_tax MONEY NOT NULL,
  other_income MONEY NOT NULL,
  net_income MONEY NOT NULL,
  total_tax MONEY NOT NULL,
  tax_percent_income DECIMAL(5, 2) CHECK (
    tax_percent_income < 100.1
    AND tax_percent_income > 0
  ),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS expenditure (
  id UNIQUE SERIAL,
  date DATE NOT NULL,
  category TEXT CHECK (LENGTH (category) < 100),
  amount MONEY NOT NULL
);

CREATE TABLE IF NOT EXISTS net (
  id UNIQUE SERIAL,
  date DATE NOT NULL,
  checking MONEY,
  savings MONEY,
  ira MONEY,
  k401 MONEY,
  hsa MONEY,
  asset_value MONEY,
  asset_debt MONEY,
  other_debt MONEY,
);

CREATE TABLE IF NOT EXISTS house (
  id UNIQUE SERIAL,
  purchase_price MONEY,
  down_payment MONEY,
  finance_amount MONEY,
  apr DECIMAL(2, 2) CHECK (
    tax_percent_income < 99.1
    AND tax_percent_income > 0
  ),
  years INTEGER,
  monthly MONEY,
  total_interest MONEY
);

CREATE TABLE IF NOT EXISTS caps (
  date DATE NOT NULL,
  k401 MONEY,
  ira MONEY,
  hsa MONEY
);
