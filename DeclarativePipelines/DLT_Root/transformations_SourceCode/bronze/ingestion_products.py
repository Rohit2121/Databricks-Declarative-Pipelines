import dlt

#products expectations

products_rules ={
    "rule_1": "product_id is not null",
    "rule_2": "price >=0"
    }

#Ingesting Products
@dlt.table(
    name = "products_stg"
)

@dlt.expect_all_or_drop(products_rules)
def products_stg():
    df = spark.readStream.option("ignoreDeletes", "true").table("dltrohit.source.products")
    return df