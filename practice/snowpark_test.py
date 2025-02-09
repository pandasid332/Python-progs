from snowflake.snowpark import Session
import sys
import logging

# Initiate logging at info level
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%I:%M:%S')

# Snowpark session
def get_snowpark_session() -> Session:
    connection_parameters = {
        "ACCOUNT": "NJOAQZY-UN57409",  # Include region if necessary
        "USER": "snowpark_user",
        "PASSWORD": "Test@12$4",
        "ROLE": "SYSADMIN",
        "DATABASE": "SNOWFLAKE_SAMPLE_DATA",
        "SCHEMA": "TPCH_SF1",
        "WAREHOUSE": "snowpark_etl_wh"
    }
    # Creating Snowflake session object
    return Session.builder.configs(connection_parameters).create()

def main():
    session = None
    try:
        session = get_snowpark_session()
        logging.info("Snowflake session created successfully.")

        # Query current context
        context_df = session.sql("SELECT current_role(), current_database(), current_schema(), current_warehouse()")
        context_df.show()

        # Query customer data
        customer_df = session.sql("SELECT c_custkey, c_name, c_phone, c_mktsegment FROM snowflake_sample_data.tpch_sf1.customer LIMIT 10")
        customer_df.show()

    except Exception as e:
        logging.error("An error occurred: %s", e)

    finally:
        if session is not None:
            session.close()
            logging.info("Snowflake session closed.")

if __name__ == '__main__':
    main()
