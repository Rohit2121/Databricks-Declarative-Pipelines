from pyspark import pipelines as dp

# Sales expectations
sales_rules = {
    "rule1": "sales_id is not null"
}

# Create empty streaming table
dp.create_streaming_table(
    name="sales_stg",
    expect_all_or_drop=sales_rules
)

# Creating East sales flow
@dp.append_flow(target="sales_stg")
def east_sales():
    df = spark.readStream.table("dltrohit.source.sales_east")
    return df

# Creating West sales flow
@dp.append_flow(target="sales_stg")
def west_sales():
    df = spark.readStream.table("dltrohit.source.sales_west")
    return df