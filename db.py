"""Testing duckdb"""
import duckdb

duckdb.sql("SELECT container_number FROM 'transfer.csv'").write_parquet("transfer.parquet")
