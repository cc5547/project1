from ChoiceArea import GetSideBar
from Data import GetData

class GetResult:
    def __init__(self) -> None:
        self.df = GetData().result_data()
        self.area, self.choice, self.address = GetSideBar().result_sidebar()

    def choice_address(self) : 
        if self.choice is not None and "" : return self.plus_index(self.df[self.df['시, 군'] == self.choice])
        elif self.address is not None : return self.plus_index(self.df[(self.df['시, 군'] == self.choice) & (self.df['글램핑장'].str.contains(self.address))])
        else : return None

    def plus_index(self, result) :
        result = result.iloc[:, 2:].sort_values('평점', ascending=False)
        result = result.reset_index(drop=True)
        result.index += 1
        
        if result.empty : result.loc[0] = ["-"] * len(result.columns)
        else : pass
        
        return result
    
    def result_function(self) : return self.choice_address(), self.area, self.choice, self.address

    # 테스트 끝나면 위에 지울 것
    # def result_function(self) : return self.choice_address()

    