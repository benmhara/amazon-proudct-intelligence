-- =====================================================
-- SCHEMA CREATION
-- =====================================================

USE DATABASE amazon_product_intelligence;

-- Medallion Architecture Schemas
CREATE OR REPLACE SCHEMA bronze;
CREATE OR REPLACE SCHEMA silver;
CREATE OR REPLACE SCHEMA gold;

-- AI Layer
CREATE OR REPLACE SCHEMA ai;

-- Analytics Layer
CREATE OR REPLACE SCHEMA analytics;

-- Governance & Security
CREATE OR REPLACE SCHEMA governance;

-- Sandbox / experimentation
CREATE OR REPLACE SCHEMA sandbox;

-- Verify
SHOW SCHEMAS;