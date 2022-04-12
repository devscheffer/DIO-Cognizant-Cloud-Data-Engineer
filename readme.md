DIO

usar pandera para a validação de schema de dataframe
```python
import pandera as pa
schema = pa.DataFrameSchema(
    columns={
        "<column_name>":pa.Column(pa.Int)
    }
)
schema.validate(df)
```
