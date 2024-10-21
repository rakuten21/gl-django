CREATE TABLE chart_of_accounts (
    id SERIAL PRIMARY KEY,  -- auto incrementing id
    account_code INT UNIQUE NOT NULL,  -- unique account code
    account_description VARCHAR(255) UNIQUE NOT NULL,  -- unique account description
    account_type account_type_enum NOT NULL,  -- account type using ENUM
    nature_of_log nature_of_log_enum NOT NULL,  -- nature of log using ENUM
    account_status BOOLEAN DEFAULT TRUE,  -- default is active (1 for active, 0 for inactive)
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,  -- stores user time for creation
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP  -- stores user time for updates
);

-- Creating trigger to automatically update 'updated_at' column
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_timestamp_trigger
BEFORE UPDATE ON chart_of_accounts
FOR EACH ROW
EXECUTE PROCEDURE update_timestamp();