'''
import dlt

#create streaming table
@dlt.table(
    name = "first_stream_table"
)
def first_stream_table():
    df = spark.readStream.table("dltrohit.source.orders")
    return df

#materialized view
@dlt.table(
    name = "first_mat_view"
)
def first_mat_view():
    df = spark.read.table("dltrohit.source.orders")
    return df


#batch view

@dlt.view(
    name = "first_batch_view"
)
def first_mat_view():
    df = spark.read.table("dltrohit.source.orders")
    return df

#create streaming view
@dlt.view(
    name = "first_streaming_view"
)
def first_streaming_view():
    df = spark.readStream.table("dltrohit.source.orders")
    return df

'''
