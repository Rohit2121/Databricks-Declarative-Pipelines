import dlt

#Customers Expectations
customers_rules ={
    "rule_1": "customer_id is not null",
    "rule_2": "customer_name is not null"
    }


#Ingesting Products
@dlt.table(
    name = "customers_stg"
)
@dlt.expect_all_or_drop(customers_rules)

def customers_stg():
    df = spark.readStream.table("dltrohit.source.customers")
    return df