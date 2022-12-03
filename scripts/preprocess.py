class preprocess:
    def __init__(self) -> None:
        pass
    
    def drop_null(self,df):
        return df.na.drop()
    
    def drop_column(self,df,column):
        return df.drop(column)